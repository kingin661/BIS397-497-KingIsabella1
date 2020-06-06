# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:48:49 2020

@author: Bella
"""
#Midterm Practice - Exercise 2.15
number1 = float((input('Enter your first number: ')))
number2 = float((input('Enter your second number: ')))
number3 = float((input('Enter your third number: ')))

if number1 >= number2 and number1 >= number3: 
    if number2 >= number3:
        print(number3,number2,number1)
    else:
        print(number2,number3,number1)

if number2 >= number1 and number2 >= number3:
    if number3 >= number1: 
        print(number1,number3,number2)
    else:
        print(number3,number1,number2)

if number3 >= number1 and number3 >= number2:
    if number1 >= number2:
        print(number2,number1,number3)
    else:
        print(number1,number2,number3)