# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:25:00 2020

@author: Bella
"""
#Assignement 3 - Exercise 5.20 


empty_table=[[1,2,3],[4,5,6],[7,8,9]]


def display_table(items):
    for i, row in enumerate(empty_table):
        for j, item in enumerate(row):
            print(f'{j}', end = ' ') 
    print()
    for row in empty_table: 
        for item in row: 
            print (item, end = ' ')
        print () 

display_table(empty_table)