from os import system
import time

def render(garden2d, budget): 
    print()
    system ("cls")
    count = 0
    cp =0
    pl =0
    print (f"BALANCE: {budget:8.2f}$")
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

def planted(action, garden2d, budget, pl):
    if action  == 1:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        
        if idx > len(garden2d[ground])-1:
            render(garden2d)
            return 
        if garden2d[ground][idx] == '🌰':
            garden2d[ground][idx] = '🌱' 
            budget -= pl
        render(garden2d,budget)
        return budget
def watering(action, garden2d, budget, wr):
    if action  == 2:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        if idx > len(garden2d[ground])-1:
            render(garden2d, budget)
            return 
        note = 0
        for ir in reversed(range(ground)):
            if garden2d[ir][idx] == '⛅' and garden2d[ground][idx] =='🌱':
                garden2d[ir][idx] = '💦'
                render(garden2d, budget) 
                time.sleep(1.2)
                garden2d[ir][idx] = '🍊'
                budget -= wr 
                render(garden2d, budget) 
                break
            elif garden2d[ground][idx] =='🌰':
                render(garden2d, budget)
                note = 1
                break
            elif garden2d[0][idx] == '🍊' :
                render(garden2d, budget)
                note = 2 
    return note, budget 

def collect(action, garden2d, budget, cl):
    if action  == 3:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        if idx > len(garden2d[ground])-1:
            render(garden2d, budget)
            return
        note = 0
        for ir in (range(ground)):
            if garden2d[ir][idx] == '🍊' and garden2d[ground][idx] =='🌱':
                garden2d[ir][idx] = '⛅'
                budget +=cl 
                render(garden2d, budget) 
                break
            elif garden2d[ground][idx] =='🌰':
                render(garden2d, budget)
                note = 1
                break
            elif garden2d[ground][idx] =='🌱' and garden2d[ground-1][idx] == '⛅':
                render(garden2d, budget)
                note = 2
                break
    return note, budget 
def cutting(action, garden2d, bd):
    if action  == 4:
        idx = int(input("Where: "))
        ground = len(garden2d)-1
        if idx > len(garden2d[ground])-1:
            render(garden2d, bd)
            return
        note = 0
        for ir in (range(ground)):
            if  garden2d[ground][idx] =='🌱':
                garden2d[ground][idx] = '🌰'
            garden2d[ir][idx] = '⛅' 
        render(garden2d,bd) 
        
                        
        
            
        
  
