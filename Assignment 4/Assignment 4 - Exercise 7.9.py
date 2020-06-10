# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:47:44 2020

@author: Bella
"""
#Assignment 4 - Exercise 7.9 
import numpy as np 

array = np.arange(1,16,1).reshape(3,5)
print(array)
print()

#a
print('A')
print(array[2])
print()

#b
print('B')
print(array[:,4])
print()

#c 
print('C')
print(array[0:2])
print()

#d 
print('D')
print(array[:, 2:5])
print()

#e
print('E')
print(array[1,4])
print()

#f
print('F')
print(array[1:3,(0,2,4)])