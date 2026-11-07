# Treasure Island - A Text-Based Adventure Game

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island!\n")
print("Your mission is to find the hidden pirate treasure.\n")

# First decision: Sneak past the guards or wait until nightfall.
user_choice = input(
    "You begin your journey at a dock guarded by the navy.\n"
    "What do you do?\n"
    "Wait until nightfall or sneak your way through?\n"
    "(S - Sneak / W - Wait): "
).lower()

if user_choice == "w":
    print("Good choice! The guards got sleepy, and you passed through...\n")

    # Second decision: Continue sailing or stop at a nearby island.
    user_choice = input(
        "You set off on your journey, but the weather seems bad.\n"
        "What do you do?\n"
        "Continue sailing or stop at the nearby island?\n"
        "(S - Stop at the island / C - Continue sailing): "
    ).lower()

    if user_choice == "s":
        print(
            "Smart choice! But now you must settle for the treasure "
            "on this island, as you have no resources for a longer journey...\n"
        )

        # Final decision: Choose one of the three doors.
        user_choice = input(
            "You stand before three doors...\n"
            "A red door, a blue door, and a yellow door.\n"
            "Only one leads to the treasure. Choose wisely!\n"
            "(R - Red / B - Blue / Y - Yellow): "
        ).lower()

        if user_choice == "y":
            print(
                "Well, aren't you a lucky sailor! You found the treasure...\n"
                "YOU WIN!"
            )
        elif user_choice == "r":
            print(
                "Oh my! You should not have opened the red door of doom.\n"
                "Now spend the rest of your life in the abyss...\n"
                "YOU LOSE!"
            )
        else:
            print(
                "Oh my! You opened the blue door of beasts.\n"
                "Now you're nothing but food, lmao...\n"
                "YOU LOSE!"
            )
    else:
        print(
            "Brave, but foolish...\n"
            "You caused your ship to drown in the storm...\n"
            "YOU LOSE!"
        )
else:
    print(
        "Brave, but foolish...\n"
        "Your sloppy attempt to sneak in failed, and you got caught...\n"
        "YOU LOSE!"
    )
