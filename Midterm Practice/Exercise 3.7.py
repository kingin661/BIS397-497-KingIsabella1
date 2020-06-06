# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:07:48 2020

@author: Bella
"""
#Midterm Practice - Exercise 3.7

print('number', 'square' , 'cube')
for number in range(0,6,1):
    print(f'{number:>6.0f}{number ** 2:>7.0f}{number **3:>5.0f}')