# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used GitHub Copilot as a teammate. One correct suggestion was to move the game rules into `logic_utils.py` and test them separately from the Streamlit interface. This was correct because the app and the tests could then use the same functions for guesses, hints, ranges, and scores. I verified it by running the game logic tests and seeing that all six tests passed.

One suggestion I did not accept as written was to put the new test in `test/test_game_logic.py`. I kept it in the existing `tests/test_game_logic.py` folder because that is the project convention and pytest already looks there. The suggestion was not necessarily wrong, but changing the folder would have made the project less consistent. I verified my choice by running the tests and seeing that all six passed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided the repairs worked when the game logic tests passed without errors. I ran `python3 -m pytest tests/test_game_logic.py`, and all six tests passed. One test makes a high guess, a low guess, and a winning guess using the same secret number, so it checks that the secret stays the right type every time. AI helped me create this test so I could check the bug again instead of only playing the game once.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
