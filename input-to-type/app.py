from os import system

def inputInt():
    n = input("Integer >> ")
    if  n.isdigit():
        n = int(n)
        print("Integer:",n)
        return n
    else:
        print("The value entered is not integer")

def inputFloat():
    n = input("Float >> ")
    try:
        n = float(n)
        return n
    except ValueError:
        print("The value entered is not float")  
 
def inputBoolean():
    n = input("Boolean True = 't', False 'f' >> ")
    if n == "t": 
        n = bool(1)
        return n
    elif n == "f":
        n = bool(0)
        return n 
    else:
        print("The value entered is not Boolean")   
        
system("cls")          
n = inputInt()
m = inputFloat()
c = inputBoolean()

if n == None or m == None :
    print ("Exit")
else:
    print ("Result: ", n+m, c)
