# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:30:50 2020

@author: Bella
"""
#Assignment 4 - Exercise 7.3 
import numpy as np

array_1 = np.arange(2,19,2).reshape(3,3)


array_2 = np.arange(9,0,-1).reshape(3,3)

print(array_1)
print()
print(array_2)

array_3 = array_1 * array_2 
print()
print(array_3)