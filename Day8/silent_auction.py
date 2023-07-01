import os


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
dic = {}
auction = True
winner = ""
highest = 0
while auction:
    print("Welcome to the silent auction :D ")
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    dic[name]=bid

    resp = input("Is there anyone one else that wants to bid? (y/n):   ").lower()
    if resp == "y":
        os.system('clear')
        continue
    else:
        auction = False 

for key in dic:
    
    if highest < dic[key]:
        highest = dic[key]
        winner = key
    else:
        continue
print(f"The winner of the silent auction is {winner}")    
