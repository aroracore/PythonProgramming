# Tip Calculator

print("Welcome to the Tip Calculator!")

bill = float(input("Enter the bill amount: "))
total_people = int(input("Enter the number of people to split the bill among: "))
tip = int(input("How much tip would you like to give (10, 12, 15): "))

# Calculate the final bill per person, including the tip.
final_bill = (bill + (bill * (tip / 100))) / total_people

print(f"Your final bill to pay is ${final_bill:.2f}")
