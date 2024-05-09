from data import garden, budget, pl, wr, cl
from lib import *

bd = budget
render(garden,bd)
while True:
    opt = menu()
    if opt == 1:
        bd = planted(opt, garden, bd, pl)
    elif opt == 2: 
        n = watering(opt, garden, bd, wr)
        bd = n[1]
        if n[0] == 1:
            print ('😠 First they plant !')
        elif n[0]==2:
            print ('😮 Stop limit!')       
    elif opt == 3:
        n = collect(opt, garden, bd, cl)
        bd = n[1]
        if n[0] == 1:
            print ('😠 First they plant !')  
        elif n[0]==2:
            print ('😕 There are no more fruits !')      
    elif opt == 4:
        cutting(opt, garden, bd)     
    elif opt == 0:    
        break 
    #########################555555555555