# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:01:03 2020

@author: Bella
"""
#Midterm Practice - Exercise 3.5 
# fig02_01.py
"""Compare integers using if statements and comparison operators."""

print('Enter two integers and I will tell you', 
      'the relationships they satisfy.')

# read first integer
number1 = int(input('Enter first integer: '))

# read second integer
number2 = int(input('Enter second integer: '))

if number1 == number2:
    print(number1, 'is equal to', number2)
else:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)
elif number1 > number2:
    print(number1, 'is greater than', number2)
else:
    print()

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)
else:
    print(number1, 'is greater than or equal to', number2)

