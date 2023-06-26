#Simple rock paper scissors game implementing the use of 
#Random module and a list: 
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lst = [rock, paper, scissors]
game = True
#taking in the user input and spitting out their choice and selection. 
print("Hi and welcome to Rock,Paper,Scissors! Can you beat the computer?")
while game:
    choice = int(input("What do you chose? 0 for Rock, 1 for Paper, 2 for Scissors: "))
    print(f"You selected!\n {lst[choice]}")
    cmpChoice = random.randint(0,2)
    print(f"The computer has picked\n {lst[cmpChoice]}")

    if choice == cmpChoice: 
        print("Looks like we have ourselves a draw.")
    elif choice == 0 and cmpChoice == 1:
        print("Looks the computer got the better of you!")
    elif choice == 0 and cmpChoice == 2:
        print("You won, look at you little go getter!")
    elif choice == 1 and cmpChoice == 0:
        print("Hey you beat the computer!!")
    elif choice == 1 and cmpChoice == 2:
        print("Looks like te computer out smarted you.. Try again..")
    elif choice == 2 and cmpChoice == 0:
        print("The computer takes this round come back again.. . ")
    elif choice == 2 and cmpChoice == 1:
        print("You are the champion my friend.. ")

    goAgain = input("Do you want to play again? Y/N:  ").lower()
    if goAgain == "y":
            continue
    else:
        print("See you later!")
        game = False
        