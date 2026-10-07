# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Ran fine for the most part where a new number was being generated and you were able to guess it and get a response for it.  But a few bugs were present such as the Difficulty changes not changing instruction range, the "New Game" button not working as intended, and the hint button resulting in opposite hints.


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
On settings, the range for each of the difficulties didn't match the range in the instructions.  So the range in the instructions is not updating as difficulty changes.

If you win or lose, and press "New Game", a new game starts but your status as having already win does not change, so you have to reload the whole thing.  I suspect it has something to do with resetting the attempts counter, or similar.

The answer/ "secret" also not changing as the difficulty updates, so it doesn't assume the ranges it is supoosed to.  I suspect it has something to do with the effective range of the game staying the same throughout regardless of the difficulty and secret not updating on difficulty changing.  You can possibly just run "New Game" when difficulty is changed.
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|"New Game" button after a win or loss|A new game starts with attempts resetted and new "secret" assigned. |The attempts never reset. |Freeze of You have Won or You have Lost|

|Changing Difficulty |The ranges change as the difficulty changes, of the instruction and the secret. | The range of the instructions given to the player and the secret doesn't assume the range of the updated difficulty. |none, just does not update. | 
| | | | |  

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One AI suggestion that was correct was when the session_state_status is set to "playing" after clicking the NEW GAME.  I verfied this by running the NEW GAME button, and finally the game was resetting/ a new game started rather than being frozen on the you won or you lost screen.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
AI wanted to change each factor one by one rather than just simply running the reset/ new game button.  I ended up asking it to do the latter.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I mainly ran the program again and tested to see if it was now working.  For example, now clicking on the NEW GAME button wasnt freezing the screen, the range was changing with the different difficulty selection, so thats how i could tell it was working.  This specifically AI didnt really have much contribution in since it was quite apparent. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Reruns is basically the program running all the way from the start after each change/ click.  Session state is basically the variables that change from the user initiated change and stay that way so that when the next rerun runs, the changes from the previous run are saved.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  It would most likely be to integrate and feed AI right into the workspace (before I was using it in the browser).  Also prompting AI to propose changes, asking it to explain each change, running it through my head and then approving it to make those changes in the file is something I did that I would most likely implement in future projects.
- What is one thing you would do differently next time you work with AI on a coding task?  Not being completely trusting of AI.  In the beginning I sort of didn't look through everything completely thoroughly, and realized that was kind of a mistake.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I now feel the power of AI generated code where AI can make direct changes directly to your files.  But I also now do realize of completely understanding all of your code first, and treating AI like a junior (to you) developer who does eveyrhting but you have to test it and give it the final approval.
