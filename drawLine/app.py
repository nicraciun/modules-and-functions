
length = int(input("length >> "))
direction = input ("direction 'v' or 'h' >> " )

def drawLine( length, direction ):

    if direction == "v":
       for i in range(length):
          print("|")
    elif direction == "h":
       for i in range(length):
          print("-",end="")
drawLine( length, direction )