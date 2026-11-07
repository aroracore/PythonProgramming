# Rock, Paper, Scissors

import random

print("Welcome to Rock, Paper, Scissors!")

choices = ["r", "p", "s"]

# Get the player's choice and generate the computer's choice.
user_choice = input(
    "What do you choose?\n"
    "Rock (r), Paper (p), or Scissors (s): "
).lower()

comp_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {comp_choice}")

# Compare choices to determine the winner.
if user_choice == comp_choice:
    print("You and the computer chose the same thing. It's a draw!")

elif user_choice == "r" and comp_choice == "p":
    print("You picked rock, but the computer picked paper...\nYOU LOSE!")

elif user_choice == "r" and comp_choice == "s":
    print("You picked rock and defeated the computer's scissors!\nYOU WIN!")

elif user_choice == "p" and comp_choice == "r":
    print("You picked paper and defeated the computer's rock!\nYOU WIN!")

elif user_choice == "p" and comp_choice == "s":
    print("You picked paper, but the computer picked scissors...\nYOU LOSE!")

elif user_choice == "s" and comp_choice == "p":
    print("You picked scissors and defeated the computer's paper!\nYOU WIN!")

elif user_choice == "s" and comp_choice == "r":
    print("You picked scissors, but the computer picked rock...\nYOU LOSE!")

else:
    print("Invalid choice! Please choose r, p, or s.")
