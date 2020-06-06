# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:25:00 2020

@author: Bella
"""
#Assignement 3 - Exercise 5.20 

empty_table=[[1,2,3],[4,5,6],[7,8,9]]


def display_table(items):
    for i in range(len(empty_table[0])):
                print(f'\t({i})', end = ' ')
    print ()
    for k in range(len(empty_table)):
        print(f'({k})', end = ' ')
        for j in range(len(empty_table[0])):
            print(f'{empty_table[k][j]:<7}', end = ' ')
        print()
        
display_table(empty_table)