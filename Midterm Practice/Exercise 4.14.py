# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:50:22 2020

@author: Bella
"""
#Midterm Pratice - Exercise 4.14
import random as rand 

number1 = rand.randrange(0,10)

number2 = rand.randrange(0,10)

answer = number1 * number2 

student_answer = int(input(f'How much is {number1} times {number2}? '))

while student_answer != answer :
    if student_answer > answer or student_answer < answer:
        print('No. Please try again.')
        student_answer = int(input(f'How much is {number1} times {number2}? '))
else:
    print('Very Good!')
    number1 = rand.randrange(0,10)
    number2 = rand.randrange(0,10)
    answer = number1 * number2 
    student_answer = int(input(f'How much is {number1} times {number2}? '))