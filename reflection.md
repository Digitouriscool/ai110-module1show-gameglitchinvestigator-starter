# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  1) The hints don't function properly. There seems to be no validation and it appears randomized, for instance I'm able to guess numbers outside the range of 0 to 100.
  2) After completing the game, we're unable to start a new game as the "New Game" button does not work. Clicking the "New Game" button only randomizes the secret, everything else (attempts, score, etc.) remains the same.
  3) I expected there to be more attempts as the program decreased in difficulty. However we get more attempts in normal mode (7) than in easy mode. 
  4) The attempts counter doesn't decrement properly. The first guess does not decrement it. For example in normal mode, we get 7 attempts (however on the left-hand pane it says 8). The first guess is not tracked. 
  5) The range of numbers was smaller for hard (1-50) than it was for normal (1-100).

  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 60 |      "Too Low"             "Go LOWER"          none
| 100 |     "Too High"            "Go HIGHER"         none
| 101 |     "Too High"            "Go HIGHER"         none

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I utilize Claude for this assignment.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI was correct in identifying that the hard range (1-50) was narrower than normal, thereby making it easier. It suggested changing the range to 1-200, which was a great idea.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When refactoring the logic and moving it over to the logic_utils.py file, the AI created a separate .py file to call the componenets of it. This was unnecessary and so I instead imported logic_utils.py in app.py, which gave access to the needed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 
    For each suggested fix, I re-ran the app and tested it manually. 

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code. 
   The number of attempts did not decrement after the first guess, This showed that the attempts was initializing to 1 and consumed an attempt before a guess.
  
- Did AI help you design or understand any tests? How?
    I used to design all the pytest files for the identified bugs. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
