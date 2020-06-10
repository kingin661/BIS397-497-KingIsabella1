# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:38:44 2020

@author: Bella
"""
#Assignment 4 - Exercise 7.5 
import numpy as np 

array_1 = np.full((2,3),2)
array_2 = np.arange(0,6).reshape(2,3)

x = array_1 ** array_2 
print('Oringal array\n', x)
print() 

flattened_x = x.flatten()
print('Flattened array\n', flattened_x)
print()
print('Oringal array\n', x)
print()

raveled_x = x.ravel()
print('Raveled array\n', raveled_x)
print()
print('Oringal array\n', x)
