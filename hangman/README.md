# 🎮 Hangman Game — CodeAlpha Internship

This is a text-based Hangman Game built in Python for the **CodeAlpha Python Programming Internship**.  
The game gives the player a clue, reveals one letter, and gives 7 lives to guess the rest of the word.

---

## ✨ Features

- Random word selection with an associated clue
- One random letter revealed at the start
- Tracks:
  - Correct guesses  
  - Incorrect guesses  
  - Lives remaining  
- Prevents duplicate inputs
- Allows multiple rounds without restarting
- Simple and beginner-friendly design

---

## 🧠 Game Logic

The game:

1. Selects a word + clue at random  
2. Reveals one letter across all positions  
3. Accepts user guesses (one letter at a time)  
4. Updates the displayed word state  
5. Deducts lives for incorrect guesses  
6. Ends when:
   - All letters are guessed → **Win**
   - Lives reach 0 → **Lose**

The logic is implemented using:

- `random` — for selecting word and index  
- Lists — to maintain guessed state  
- Loops and conditionals — for gameplay flow  

---

## ▶️ How to Run

```
python hangman.py
```

Then choose:

```
1 → Play
2 → Exit
```

The game resets after every round.

---

## 📁 Project Info

- **Internship:** CodeAlpha – Python Programming  
- **Task:** Hangman Game  
- **Developer:** Janakisetty Mukesh Babu
