# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:06:56 2020

@author: Bella
"""
#Assignment 2 Exercise 3.1
passes = 0
failures = 0

for student in range(10):
    result = int(input('Enter Result (1=pass, 2=fail): '))
    
    if result != 1 or result != 2:
        result = int(input('Enter Result (1=pass, 2=fail): '))
    if result ==1: 
        passes = passes + 1 
    
failures = 10 - passes 
        
        
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor.')

