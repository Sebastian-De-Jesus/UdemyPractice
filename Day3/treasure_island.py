#very simple treasure island experience with three questions of hopes of finding the treasure chest:

gameon = True
while(gameon):
    openchest = '''*******************************************************************************
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
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************'''
    print(openchest)

    print("Welcome to Treasue Island.\n Your mission is to find the treasure.\n")
    choice = input("You'e at a cross road. Where do you want to go? Type 'left' or 'right'\n")
    if choice == "left":
        choiceTwo = input("You come to a lake. there is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n")
        if choiceTwo== "wait":
            choiceThree = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n")
            if choiceThree == "yellow":
                print(openchest)
                print("You found the treasure!")
            else:
                print("You've open the door to a vampire... You're now food. . . .")
        else: 
            print("Though you tried valiantly you were swept away by the current.")
    else:
        print("You've picked the wrong path..... sorry friend... Game over...")
    value = input("Want to go again? yes or no? ")
    if value == "yes":
        continue
    else:
        gameon = False
    
        