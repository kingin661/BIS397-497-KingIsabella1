# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:25:01 2020

@author: Bella
"""
#Assignment 2 Exercise 4.12

import random as rand
 
finish_line = 70

def tortoise_move(tortoise):
    i = rand.randrange(1,11)
    #Moving the tortoise
    if i >= 1 and i <= 5:
        tortoise = tortoise + 3 
    elif i >= 6 and i <= 7:
        tortoise = tortoise - 6 
    elif i >= 8 and i <= 10:
        tortoise = tortoise + 1 
    #to ensure tortoise doesn't go behind or ahead of finish line  
    if tortoise < 1:
        tortoise = 1 
    elif tortoise > finish_line: 
        tortoise = finish_line 
        
    return tortoise

def hare_move(hare):
    i = rand.randrange(1,11) 
    #Moving the hare
    if 1 <= i <= 2:
        hare = hare + 0 
    elif 3 <= i <= 4: 
        hare = hare + 9 
    elif 5 <= i <= 5: 
        hare = hare - 12 
    elif 6 <= i <= 8:
        hare = hare + 1 
    elif 9 <= i <= 10: 
        hare = hare - 2 
# the hare's moves 
    if hare < 1: 
        hare = 1
    elif hare > finish_line: 
        hare = finish_line 
        
    return hare
# to ensure that hare doesn't go behind or ahead of finish 

def race_positions(tortoise, hare):
    for count in range (1, finish_line +1):
        if count == tortoise and count == hare: 
            print('OUCH!!', end=' ')
        elif count == hare: 
            print('H', end=' ')
        elif count == tortoise: 
            print('T', end=' ')
        else: 
            print(' ', end=' ')
    print()

tortoise = 1 
hare = 1 
clock = 0

print ("BANG !!!! ")
print ("AND THEY'RE OFF !!!! ")

while tortoise < finish_line and hare < finish_line:
    tortoise = tortoise_move(tortoise)
    hare = hare_move(hare)
    race_positions(tortoise, hare)
    clock = clock + 1
   
if tortoise >= hare: 
    print(f'\nTORTOISE WINS!!! YAY!!\nTime Elasped = {clock} seconds')
if tortoise == hare: 
    print(f"\nWow! It's a tie.\nTime Elasped = {clock} seconds")
else: 
    print(f"\nHare wins. Yuch Time Elasped = {clock} seconds")
    
