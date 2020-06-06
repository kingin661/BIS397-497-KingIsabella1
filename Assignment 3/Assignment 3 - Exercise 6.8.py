# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:55:21 2020

@author: Bella
"""
#Assignment 3 - Exercise 6.8 

def num_to_word(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000

    assert(0 <= num) #To make num always greater than 0 

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred ' + num_to_word(num % 100)

    if (num < m):
        if num % k == 0: return num_to_word(num // k) + ' thousand'
        else: return num_to_word(num // k) + ' thousand, ' + num_to_word(num % k)
      
amount = input('Enter your check amount: ')
number = int(float(amount))
if number >= 1000:
    print('That number is too high, try something lower than one thousand.')
    amount = input('Enter your amount again:')


list_= amount.split('.')
if len(list_)==2 :
   print(num_to_word(int(list_[0])).upper(),"AND",list_[1],"/",10**(len(list_[1])))
else :
   print(num_to_word(int(list_[0])).upper())