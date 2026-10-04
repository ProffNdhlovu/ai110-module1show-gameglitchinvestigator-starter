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

- [x] The game asks the user to guess a secret number. It gives a hint after each guess and keeps track of the score.
- [x] I found that the secret number changed when the Submit button was clicked, so it was hard to win. The Higher and Lower hints were also incorrect.
- [x] I stored the secret number and other game values in Streamlit session state. I moved the guessing rules into `logic_utils.py` and added tests to make sure the guesses, hints, attempts, and score work correctly.

## Demo Walkthrough

This sample uses Normal difficulty with a secret number of 50:

1. The user enters a guess of 40.
2. The game returns `Too Low` and updates the score after the first attempt.
3. The user enters a guess of 70.
4. The game returns `Too High` and updates the score after the second attempt.
5. The user enters a guess of 50.
6. The game returns `Win`, displays the final score, and ends the game.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
