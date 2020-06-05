# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:24:44 2020

@author: Bella
"""
#Assignment 3 Exercise 5.5 
alphabet = []

alphabet_ = 'abcefghijklmnopqrstuvwxyz'

alphabet.extend(alphabet_)

#a 
a = alphabet[0:13]
print ('\na\n')
print (a)

#b 
b = alphabet[:13]
print ('\nb\n')
print (b)

#c 
c = alphabet[12:25]
print ('\nc\n')
print (c)

#d 
d = alphabet[-13:]
print ('\nd\n')
print (d)

#e 
e = alphabet[::2]
print('\ne\n')
print (e)

#f
alphabet.sort(reverse=True)
print ('\nf\n')
print(alphabet)

#g
g = alphabet[::3]
print('\ng\n')
print (g)
