# BMI Calculator

print("Welcome to the BMI Calculator!")

user_height = float(input("Enter your height (in meters): "))
user_weight = float(input("Enter your weight (in kg): "))

final_height = user_height ** 2
user_bmi = user_weight / final_height

print(f"Your BMI is {user_bmi:.2f}!")

if user_bmi < 18.5:
    print("You are underweight! Go eat something...")
elif user_bmi > 25:
    print("You are overweight! Consider a balanced diet...")
else:
    print("You have a healthy BMI!")
