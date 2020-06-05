#Assignment 2 - Exercise 2.12
p = 100
r = .07
n = 10
a = p*(1+r) ** n
print (f'After 10 years: ${a:.2f}')
p = a
b = p * (1 +r) ** n
print(f'After 20 years: ${b:.2f}')
p = b 
c = p * (1+r) ** n
print(f'After 30 years: ${c:.2f}')

