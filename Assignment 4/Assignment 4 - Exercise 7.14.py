# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:56:26 2020

@author: Bella
"""
#Assignment 4 - Exercise 7.14
import numpy as np

array1 = np.array([[0,1],[2,3]])
array2 = np.array([[4,5],[6,7]])

#a
print('A')
array3 = np.vstack((array1,array2))
print(array3)
print()

#b
print('B')
array4 = np.hstack((array1,array2))
print(array4)
print()

#c
print('C')
array5 = np.vstack((array4,array4))
print(array5)
print()

#d
print('D')
array6 = np.hstack((array3,array3))
print(array6)