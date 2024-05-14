from tax import *
p = 0
while True:
    print ("-"*40) 
    amount = int(input("Amount >> "))
    goal = int(input("Goal (Salary = 1, loan = 2, Donation = 3, Exit = any key) >> "))
    print ("#"*40) 
    if goal == 1 or goal == 2 or goal == 3:
        tax = calculateTax(amount, goal)
        if tax[3] == 1:
            print ("Calculation from salary")   
        if tax[3] == 2:
            print ("Calculation from loan")   
        if tax[3] == 3:
            print ("Calculation from Donation")   
        print (F"Tax: {tax[0]:,.2f} MDL")
        print (F"Percent: {tax[1]*100:.0f} %")
        print (F"From the amount: {tax[2]:,.2f} MDL")
        print ("#"*40)
    else: 
        break