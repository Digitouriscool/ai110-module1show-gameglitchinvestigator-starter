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

- [x] **Describe the game's purpose.**
  Glitchy Guesser is a number guessing game built with Streamlit. The player selects a difficulty (Easy, Normal, or Hard), which sets a numeric range and an attempt limit. A secret number is randomly chosen within that range, and the player tries to guess it. After each guess, the game gives a hint (Too High / Too Low) and updates the score. The player wins by guessing correctly within the allowed attempts.

- [x] **Detail which bugs you found.**
  1. **Hard difficulty range too narrow** — Hard used 1–50, making it easier than Normal (1–100).
  2. **Hint messages reversed** — "Go HIGHER" showed when the guess was too high, and "Go LOWER" when too low.
  3. **Attempts initialized to 1** — The counter started at 1 instead of 0, consuming an attempt before the player guessed anything.
  4. **New game didn't fully reset** — Clicking "New Game" only cleared attempts and the secret; score, status, and history carried over.
  5. **Secret cast to string on even attempts** — Every other guess forced the secret to a string, breaking comparisons.
  6. **Score awarded points for wrong guesses** — "Too High" on even-numbered attempts added +5 instead of deducting 5.
  7. **Info banner hardcoded range** — The "Guess between 1 and 100" message ignored the actual difficulty range.
  8. **Secret not regenerated on difficulty change** — Switching difficulty kept the old secret, which could be outside the new range (e.g., secret=25 shown in Easy mode where max is 20).
  9. **Attempts counter didn't decrement on first guess** — The info banner rendered before the increment ran, so the first guess never visibly reduced the counter.
  10. **Out-of-range guesses accepted** — No validation prevented guesses outside the difficulty's range.

- [x] **Explain what fixes you applied.**
  1. Changed Hard difficulty range to 1–200.
  2. Swapped the "Go HIGHER" and "Go LOWER" hint messages.
  3. Changed the initial `attempts` value from 1 to 0.
  4. Added resets for `score`, `status`, and `history` in the new game block.
  5. Removed the even/odd type-cast logic; the secret is always passed as an int.
  6. Removed the conditional `+5` branch; "Too High" always deducts 5 points.
  7. Replaced the hardcoded range string with `{low}` and `{high}` variables.
  8. Added difficulty tracking in session state to regenerate the secret whenever the difficulty changes.
  9. Moved the info banner to after the submit block so it renders with the updated attempt count.
  10. Added `low` and `high` parameters to `parse_guess` with a bounds check that rejects out-of-range input.
  11. Refactored all four logic functions (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) from `app.py` into `logic_utils.py`.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Normal difficulty (1- 100)
2. User enters a guess of 90
3. Game returns "Go LOWER"
4. User enters a guess of 50
5. Game returns "Go HIGHER"
6. Score updates correctly after each guess
7. User enters a guess of 60
8. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
