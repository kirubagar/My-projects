
#My 1st project
# Treasure Island
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
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
print("Your mission is to find the treasure.")
# 1st level
side = input("which side you want to go right or left"
             "right for hole,left for straight way ").lower()
if side == "right":
    print("game over you fell into the hole")
    quit()
elif side == "left":
    print("you can walk")
else:
    print("enter valid input")
    quit()
# level 2
action = input("what do you want to do swim or wait"
               " swim to swim across "
               "wait to get the boat ").lower()
if action == "swim":
    print("game over you are eaten by crocodile")
    quit()
elif action == "wait":
    print("you can take the boat and cross the river")
else:
    print("enter valid input")
    quit()
#level 3
door = input("which door you have to open red,blue,yellow "
             "red door have a mystery"
             " blue door have a mystery"
             " yellow have the key ").lower()
if door == "red" or door == "blue":
    print("game over you are killed by a monster")
    quit()
elif door == "yellow":
    print("hurray you win"
          " you find the treasure")
else:
    print("enter valid input")


# share your thoughts guys



