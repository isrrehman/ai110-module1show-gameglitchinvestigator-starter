# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The game sets a range for you depending on your difficulty, and a limited number of attempts, and you are to attempt to guess the random number which exists within range.
- [ ] Detail which bugs you found.
The instructions did not always update with the difficulty changes, so the range remained not what it was supposed to be, the same with the SECRET number that was to be found.  Also the NEXT GAME button would not start another game and freeze on YOU WON or YOU LOST.
- [ ] Explain what fixes you applied.
I updated the range in the instructions, changing as the difficulty changes.  I also made sure the SECRET is always within range.  For the NEXT GAME button bug, I made sure that when you now click it, a new game actually does succesfully start and carries your score with it.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
Run the game.
2. <!-- Describe this step -->
In the instructions you will see the range from which you are to make your guesses.  When you change the difficulty, this range would also change.  (A fix I implemented.)
3. <!-- Describe this step -->
Then, as you run the game, going through your attempts.  When you finally Win or run out of attempts and lose.  You can then click the NEXT GAME button to start a fresh game while your score carries over. (Another fix I implemented.)
4. <!-- Describe this step -->
You will also notice through it all, the number always stays within the prescribed range in the instructions.  (Another fix I implemented, it used to not be in range always.)


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\student\Downloads\Project\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 14 items                                                                                                                                

tests\test_game_logic.py ..............                                                                                                     [100%]

=============================================================== 14 passed in 4.61s ===============================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
