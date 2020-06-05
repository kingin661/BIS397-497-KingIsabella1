# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:09:39 2020

@author: Bella
"""
#Assigment 3 - Exercise 5.11 


print ('Type your string and press enter. ')
letters = list(input())

letters = [item.lower() for item in letters]
  
alphabet = []

alphabet_ = 'abcefghijklmnopqrstuvwxyz'

alphabet.extend(alphabet_)


def summarize_letters(letters):
    for i in alphabet: 
        letters_summarized = (i,letters.count(i))
        if letters.count(i) > 0:
            print(f'{letters_summarized}')
    if alphabet == letters: 
        print('The whole alphabet is present.')
    else: 
        print('The whole alphabet is not present.')

summarize_letters(letters)