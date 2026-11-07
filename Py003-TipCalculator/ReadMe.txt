# 💰 Tip Calculator
A beginner-friendly Python program that calculates the total bill, including a selected tip percentage, and splits the amount equally among multiple people.

## ✨ Features
- Accepts the total bill amount.
- Allows the user to select a tip percentage (10%, 12%, or 15%).
- Accepts the number of people sharing the bill.
- Calculates the final amount each person needs to pay.
- Displays the result up to two decimal places.

## 🧮 Calculation Formula
```text
Tip Amount = Bill × (Tip Percentage / 100)
Final Bill Per Person = (Bill + Tip Amount) / Number of People
```

## 🛠️ Requirements
- Python 3.x
- No external libraries required.

## 🚀 How to Run
Execute the following command from the project directory:
```bash
python main.py
```

## 💻 Example Output
```text
Welcome to the Tip Calculator!
Enter the bill amount: 150
Enter the number of people to split the bill among: 3
How much tip would you like to give (10, 12, 15): 12
Your final bill to pay is $56.00
```

## 📚 Concepts Learned
- Variables and data types
- User input using `input()`
- Type conversion using `float()` and `int()`
- Arithmetic operators
- Percentage calculations
- Division
- F-string formatting

---

Difficulty: Beginner
Language: Python 3
