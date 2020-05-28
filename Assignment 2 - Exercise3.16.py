# -*- coding: utf-8 -*-
"""
Created on Tue May 26 23:15:34 2020

@author: Bella
"""
number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
number3 = int(input('Enter third number: '))
number4 = int(input('Enter fourth number: '))
number5 = int(input('Enter fifth number: '))
number6 = int(input('Enter sixth number: '))
number7 = int(input('Enter seventh number: '))
number8 = int(input('Enter eigth number: '))
number9 = int(input('Enter ninth number: '))
number10 = int(input('Enter tenth number: '))

print('\n')
print('Firt Highest Number Equals'\
,max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10))
    
if max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number1:
    print('The Second Highest Number Equals'\
          ,max(number2,number3,number4,number5,number6,number7,number8\
,number9,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number2:
    print('The Second Highest Number Equals'\
          ,max(number1,number3,number4,number5,number6,number7,number8\
,number9,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number3:
    print('The Second Highest Number Equals'\
          ,max(number1,number2,number4,number5,number6,number7,number8\
,number9,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number4:
    print('The Second Highest Number Equals'\
          ,max(number1,number2,number3,number5,number6,number7,number8\
,number9,number10)) 
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number5:
    print('The Second Highest Number Equals'\
          ,max(number1,number2,number3,number4,number6,number7,number8\
,number9,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number6:
    print('The Second Largest Number Equals'\
          ,max(number1,number2,number3,number4,number5,number7,number8\
,number9,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number7:
    print('The Second Highest Number'\
          ,max(number1,number2,number3,number4,number5,number6,number8\
,number9,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number8:
    print('The Second Highest Number'\
          ,max(number1,number2,number3,number4,number5,number6,number7\
,number9,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number9:
    print('The Second Highest Number Equals'\
          ,max(number1,number2,number3,number4,number5,number6,number7\
               ,number8,number10))
elif max(number1,number2,number3,number4,number5,number6,number7,number8\
,number9,number10) == number10:
    print('The Second Highest Number Equals'\
          ,max(number1,number2,number3,number4,number5,number6,number7\
               ,number8,number9))

