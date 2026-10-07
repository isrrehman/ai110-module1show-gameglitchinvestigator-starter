from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from logic_utils import check_guess, get_range_for_difficulty

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")
DIFFICULTIES = ["Easy", "Normal", "Hard"]


def run_app():
    at = AppTest.from_file(APP_PATH)
    at.run()
    return at


def click_new_game(at):
    new_game = next(b for b in at.button if b.label.startswith("New Game"))
    new_game.click().run()


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 1: "New Game" didn't reset the won/lost status, so the game stayed locked.
@pytest.mark.parametrize("finished_status", ["won", "lost"])
def test_new_game_resets_status(finished_status):
    at = run_app()
    at.session_state.status = finished_status
    at.run()

    click_new_game(at)

    assert at.session_state.status == "playing"
    assert at.session_state.history == []
    assert not any("already won" in s.value for s in at.success)
    assert not any("Game over" in e.value for e in at.error)


# Bug 1 (related): "New Game" always picked a secret from 1 to 100.
@pytest.mark.parametrize("difficulty", DIFFICULTIES)
def test_new_game_secret_matches_difficulty_range(difficulty):
    at = run_app()
    at.selectbox[0].select(difficulty).run()
    low, high = get_range_for_difficulty(difficulty)

    for _ in range(20):
        click_new_game(at)
        assert low <= at.session_state.secret <= high


# Bug 2: the instructions always said "between 1 and 100".
@pytest.mark.parametrize("difficulty", DIFFICULTIES)
def test_instructions_show_difficulty_range(difficulty):
    at = run_app()
    at.selectbox[0].select(difficulty).run()
    low, high = get_range_for_difficulty(difficulty)

    assert f"Guess a number between {low} and {high}." in at.info[0].value


# Bug 3: the secret wasn't regenerated when the difficulty changed.
def test_changing_difficulty_regenerates_secret():
    at = run_app()
    at.session_state.secret = 99  # outside the Easy range
    at.run()

    at.selectbox[0].select("Easy").run()
    low, high = get_range_for_difficulty("Easy")

    assert low <= at.session_state.secret <= high
    assert at.session_state.difficulty == "Easy"


def test_changing_difficulty_starts_fresh_game():
    at = run_app()
    at.session_state.status = "won"
    at.session_state.history = [10, 20]
    at.run()

    at.selectbox[0].select("Hard").run()

    assert at.session_state.status == "playing"
    assert at.session_state.history == []


def test_same_difficulty_keeps_secret():
    at = run_app()
    secret = at.session_state.secret

    at.run()

    assert at.session_state.secret == secret
