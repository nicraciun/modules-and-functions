percent_1 = 0.46
percent_2 = 0.36
percent_3 = 0.26

def calculateTax(amount, goal):
    if goal == 1:
        p = percent_1
        tax = amount * percent_1
    elif goal == 2:
        p = percent_2
        tax = amount * percent_2 
    elif goal == 3:
        p = percent_2
        tax = amount * percent_3 
    return tax, p, amount, goal

