# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:14:25 2020

@author: Bella
"""
#Assignment 3 - Exercise 5.15
from operator import itemgetter


#creating tuple of invoices
hardware_invoices = [(83,'Electric sander',7,57.98), 
                     (24,'Power saw',18,99.99),
                     (7,'Sledge hammer',11,21.50),
                     (77,'Hammer',76,11.99),
                     (39,'Jig saw',3,79.50)]

#a 

part_description = sorted(hardware_invoices,key=itemgetter(1)) 
print('Sorted by price description.')
print(part_description)
print('\n')

#b 

price = sorted(hardware_invoices,key=itemgetter(3))
print('Sorted by price.')
print(price)
print('\n')

#c
print('Price Description and quantity, sorted by quantity.')
description_quantity = sorted(tuple(map(lambda item: (item[1], item[2]), hardware_invoices)), key=itemgetter(1))
print(description_quantity)
print('\n')


#d
print('Price description and total value.')
seperated_invoices = tuple(map(lambda item: (item[1],(float( item[2] * item[3]))),hardware_invoices))
sorted_invoices = sorted(seperated_invoices,key=itemgetter(1))
print(sorted_invoices)
print('\n')


#e
print('Parts with values above $200 and below $500.')
for tuple in sorted_invoices :
    description, value = tuple 
    if 200 <= value <500: 
        print(tuple)
print('\n')

#f 
print('Total of all invoices.')
invoices_total = list(map(lambda item:( item[1]), sorted_invoices))
print(sum(invoices_total))