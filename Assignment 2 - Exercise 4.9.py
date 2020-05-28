# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:03:14 2020

@author: Bella
"""
#Assigment 2 Exercise 4.9 

print('Celsius    Fahrenheit')

for number in range(0,101,1):
    fahrenheit = ((9/5) * number +32)
    print(f'{number:>4} {fahrenheit:>12.0f}')