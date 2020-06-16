# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:38:11 2020

@author: Bella
"""
# Score: 18/25
# Rerolls don't seemt o do anything

import random as rand 

print("Let's play Yahtzee!")

die1 = rand.randrange(1,6)
die2 = rand.randrange(1,6)
die3 = rand.randrange(1,6)
die4 = rand.randrange(1,6)
die5 = rand.randrange(1,6)

roll_1 = [die1,die2,die3,die4,die5]


print('Your roll is')
print(f'{die1} {die2} {die3} {die4} {die5}')

reroll = input('What die do you want to roll again (seperate by commas)?\n')

rerolls = reroll.split(',')



for item in rerolls:
    die111 = die1
    die22 = die2 
    die33 = die3
    die44 = die4
    die55 = die5
    if item == 1 :     
        die111 = rand.randrange(1,6)
        die22 = die2 
        die33 = die3
        die44 = die4
        die55 = die5
        if item == 2:   
            die22 == rand.randrange(1,6)
            die33 = die3
            die44 = die4
            die55 = die5
            die111 = die1
            if item == 3:           
                die33 = rand.randrange(1,6)
                die44 = die4
                die55 = die5
                die111 = die1
                die22 = die2
                if item == 4:
                        die44 = rand.randrange(1,6)
                        die55 = die5
                        die111 = die1
                        die22 = die2 
                        die33 = die3
                        if item == 5:                         
                            die55 = rand.randrange(1,6)
                            die111 = die1
                            die22 = die2 
                            die33 = die3
                            die44 = die4
    roll_2 = [die111,die22,die33,die44,die55]
    if item == -99:
        break

print(roll_2, end = ' ')