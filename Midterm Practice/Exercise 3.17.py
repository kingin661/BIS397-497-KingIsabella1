# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:19:57 2020

@author: Bella
"""
# first triangle
for row in range(1, 11):
    for column in range(1, row + 1):
        print('*', end='')
    print()
print()

# second triangle
for row in range(10, 0, -1):
    for column in range(1, row + 1):
        print('*', end='')
    print()
print()

# third triangle
for row in range(10, 0, -1):
    for space in range(10, row, -1):
        print(' ', end='')
    for column in range(1, row + 1):
        print('*', end='')
    print()
print()

# fourth triangle
for row in range(10, 0, -1):
    for space in range(1, row):
        print(' ', end='')
    for column in range(10, row - 1, -1):
        print('*', end='')
    print()
print()



