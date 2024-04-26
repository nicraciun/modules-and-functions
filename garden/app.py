from data import garden
from lib import *

render(garden)
while True:
    opt = menu()
    if opt == 1:
        planted(opt, garden)
    elif opt == 2: 
        n = watering(opt, garden)
        if n == 1:
            print ('😠 First they plant !')
        elif n==2:
            print ('😮 Stop limit!')       
    elif opt == 3:
        n = collect(opt, garden)
        if n == 1:
            print ('😠 First they plant !')  
        elif n==2:
            print ('😕 There are no more fruits !')      
    elif opt == 4:
        cutting(opt, garden)     
    elif opt == 0:    
        break 