# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:20:43 2020

@author: Bella
"""
#Midterm Practice - Exercise 3.22
for i in range(2): #This makes it so the loop only iterates twice (w/ out a break)
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered: ', value)
    
    if value == -1: 
        break 
    else:
        print('The loop terminated wihtout executing the break.')