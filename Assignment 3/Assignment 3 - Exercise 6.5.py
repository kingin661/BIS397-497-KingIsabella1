# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:09 2020

@author: Bella
"""
#Assignment 3 - Exercise 6.5 
text = input('Input your sentence and I will count the duplicate words: ')

text_lower = text.lower() 

word_counts = { }

for word in text_lower.split():
    if word in word_counts:
        word_counts[word] += 1 
    else:
        word_counts[word] = 1 

print(f'{"Word":<12}# of Duplicates')

for word, count in sorted(word_counts.items()):
    if count > 1:
        print(f'{word:<12}{count}')
 
print('\nThe number of unique words:', len(word_counts))

