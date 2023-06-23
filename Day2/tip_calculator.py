#simple tip calculator: 
#simple function to do calculations
def calculateTip(a,b,c):
    totalPP = 0
    tipAmount = 0
    if b == 10:
        tipAmount = a*.1
        a = a+tipAmount
    elif b == 12:
        tipAmount = a*.12
        a = a+tipAmount
    elif b == 15:
        tipAmount = a*.15
        a = a+tipAmount
    elif b == 20:
        tipAmount = a*.2
        a = a+tipAmount
     
    totalPP = a/c
    return totalPP

print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, 15, 20? "))
ppl = int(input("How many people want to split the bill? "))
total = calculateTip(bill,tip,ppl)
print(f"Each individual should pay: ${total:.2f}")
    