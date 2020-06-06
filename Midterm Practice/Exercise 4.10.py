# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:30:59 2020

@author: Bella
"""
#Midterm Practice - Exercise 4.10 
import random as rand

number = rand.randrange(0,1001)


guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))

while guess != number: 
    if guess > number:
        guess = int(input('Too high. Try Again: '))
    if guess < number:
        guess = int(input('Too low. Try Again: ' ))
else:
    print('Congratulations you guessed the correct answer! ')
    
next_game = input('Do you want to play again? ')

if next_game == 'yes' or next_game == 'Yes':
    guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
    while guess != number: 
        if guess > number:
            guess = int(input('Too high. Try Again: '))
        if guess < number:
           guess = int(input('Too low. Try Again: ' ))
    else:
        print('Congratulations you guessed the correct answer! ')
elif next_game == 'no'  or next_game == 'No':
    print('Thank you for playing.')
else:
    print("Sorry I don't understand.")