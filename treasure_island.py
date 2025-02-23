print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
door = input("There are two doors in front of you."
             "One leads to treasure.\n"
             "Which door are you going to choose left or right?\n").lower()
if door == "left":
    river=input("You\'ve come across a river."
                "The treasure is in the other side of the river.\n"
                "Do you want to swim or wait?\n").lower()
    if river == "wait":
        box = input("You\'ve crossed the river."
                    "There are 3 colored boxes.\n"
                    "Which one do you want to pick red or blue or yellow?\n").lower()
        if box=="yellow":
            print("Found treasure.\nYou win")
        elif box=="red":
            print("It\'s a BOMB...just kidding.\nGame over")
        elif box=="blue":
            print("Lollipo found.\nGame over")
        else:
            print("Invalid color.\nGame over")
    else:
        print("Alligators...Patience is important.\nGame over!")
else:
    print("Just a wall.Game over!")