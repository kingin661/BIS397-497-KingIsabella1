# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:37:47 2020

@author: Bella
"""
#Midterm Practice - Exercise 2.11
number = int(input('Enter your five digit number: '))


first_number = (number // 10000) #first number 
second_number = ((number // 1000) % 10) # second number 
third_number = ((number // 100) % 10) #third number 
fourth_number = ((number // 10) % 10) # fourth number 
fifth_number = (number % 10) #last number 

print(f'{first_number}\t\t\t{second_number}\t\t\t{third_number}\t\t\t{fourth_number}\t\t\t{fifth_number}')