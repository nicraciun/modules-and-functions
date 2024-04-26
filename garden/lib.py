from os import system
import time
def render(garden2d): 
    print()
    system ("cls")
    count = 0
    cp =0
    pl =0
    for ri in range(len(garden2d)):
        for pi in range(len(garden2d[ri])):
            if garden2d[ri][pi] =="🍊":
                count +=1
            print (garden2d[ri][pi], ' ', end="")
        print("m"+str(len(garden2d) - ri), end="")
        print()
        if ri == len(garden2d)-1:
            for i in range(len(garden2d[ri])):
                if garden2d[ri][i] =='🌱':
                    cp +=1
                print(' '+str(i)+'  ', end="")
    pl =(len(garden2d)-1)*len(garden2d[1])
    plants = count*100/pl
    print()
    print(f"Fruits:{plants:3.0f}%")
    print ('plants:', cp)

def menu():
    print ("ACTION: 1-planted, 2-watering, 3-collect, 4-cutting, 0-exit")
    action = int(input("> "))
    return action

def planted(action, garden2d):
    if action  == 1:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        
        if idx > len(garden2d[ground])-1:
            render(garden2d)
            return 
        if garden2d[ground][idx] == '🌰':
            garden2d[ground][idx] = '🌱' 
        render(garden2d)

def watering(action, garden2d):
    if action  == 2:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        if idx > len(garden2d[ground])-1:
            render(garden2d)
            return 
        note = 0
        for ir in reversed(range(ground)):
            if garden2d[ir][idx] == '⛅' and garden2d[ground][idx] =='🌱':
                garden2d[ir][idx] = '💦'
                render(garden2d) 
                time.sleep(1.2)
                garden2d[ir][idx] = '🍊' 
                render(garden2d) 
                break
            elif garden2d[ground][idx] =='🌰':
                render(garden2d)
                note = 1
                break
            elif garden2d[0][idx] == '🍊' :
                render(garden2d)
                note = 2 
    return note 

def collect(action, garden2d):
    if action  == 3:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        if idx > len(garden2d[ground])-1:
            render(garden2d)
            return
        note = 0
        for ir in (range(ground)):
            if garden2d[ir][idx] == '🍊' and garden2d[ground][idx] =='🌱':
                garden2d[ir][idx] = '⛅' 
                render(garden2d) 
                break
            elif garden2d[ground][idx] =='🌰':
                render(garden2d)
                note = 1
                break
            elif garden2d[ground][idx] =='🌱' and garden2d[ground-1][idx] == '⛅':
                render(garden2d)
                note = 2
                break
    return note 
def cutting(action, garden2d):
    if action  == 4:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        if idx > len(garden2d[ground])-1:
            render(garden2d)
            return
        note = 0
        for ir in (range(ground)):
            if  garden2d[ground][idx] =='🌱':
                garden2d[ground][idx] = '🌰'
            garden2d[ir][idx] = '⛅' 
        render(garden2d) 
        
                        
        
            
        
  
