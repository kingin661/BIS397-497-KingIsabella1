# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:16:07 2020

@author: Bella
"""
#Assignment 3 - Exercise 5.28 
import statistics as stat
import numpy as nump

responses = [1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

for i in range (1,6):
    frequency = responses.count(i)
    print(f'The Frequency of {i} was {frequency}') 
print('\n')
    
print(f'The lowest response was {min(responses)}')
print('\n')
print(f'The highest response was {max(responses)}')
print('\n') 


range_ = max(responses) - min(responses)
print(f'The range of responses was {range_}.')
print('\n') 

print(f'The mean of responses was {stat.mean(responses)}.')
print('\n')

print(f'The median of responses was {stat.median(responses)}.')
print('\n')

print(f'The most occuring response was {stat.mode(responses)}.')
print('\n')

print(f'The variance of responses was {stat.variance(responses):.3}.')
print('\n')

print(f'The standard deviation of responses was {stat.stdev(responses):.3}.')
