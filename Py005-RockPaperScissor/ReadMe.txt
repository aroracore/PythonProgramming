# 🪨 Rock, Paper, Scissors
A beginner-friendly command-line Rock, Paper, Scissors game built with Python. Play against the computer, which randomly selects its move, and see who wins!

## ✨ Features
- Play Rock, Paper, or Scissors against the computer.
- Computer generates a random choice.
- Automatically determines the winner.
- Detects draws.
- Handles invalid user input.
- Supports uppercase and lowercase choices.

## 🎮 How to Play
Choose one of the following options:
| Input | Choice |
|---|---|
| `r` | Rock |
| `p` | Paper |
| `s` | Scissors |

### Game Rules
- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
- Identical choices result in a draw.

## 🛠️ Requirements
- Python 3.x
- `random` module (included in Python's standard library).
No external libraries required.

## 🚀 How to Run
Navigate to the project directory and execute:
```bash
python main.py
```

## 💻 Example Output
```text
Welcome to Rock, Paper, Scissors!
What do you choose?
Rock (r), Paper (p), or Scissors (s): r

You chose: r
Computer chose: s
You picked rock and defeated the computer's scissors!
YOU WIN!
```
*The computer's choice is randomly generated, so your results will vary.*

## 📚 Concepts Learned
- Importing modules using `import`
- Python's `random` module
- Random selection using `random.choice()`
- Lists
- Variables and user input
- Conditional statements (`if`, `elif`, `else`)
- String methods (`lower()`)
- Input validation

---

**Difficulty:** Beginner
**Language:** Python 3