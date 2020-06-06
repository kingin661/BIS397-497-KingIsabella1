# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:02:24 2020

@author: Bella
"""
import statistics as stat 
import random as rand

number1 = rand.randrange(0,11)
number2 = rand.randrange(0,11)
number3 = rand.randrange(0,11)
number4 = rand.randrange(0,11)
number5 = rand.randrange(0,11)
number6 = rand.randrange(0,11)
number7 = rand.randrange(0,11)
number8 = rand.randrange(0,11)
number9 = rand.randrange(0,11)
number10 = rand.randrange(0,11)

numbers = [number1,number2,number3,number4,number5,number6,number7,number8,number9,number10]

def descriptive(numbers) :
    print(f'The mean is {stat.mean(numbers)}')
    print(f'The meadian is {stat.median(numbers)}')
    print(f'The sample standard deviation is {stat.stdev(numbers):.2f}')
    print(f'The population standard deviation is {stat.pstdev(numbers):.2f}')
    
descriptive(numbers)