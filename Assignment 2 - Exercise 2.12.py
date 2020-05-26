#Assignment 2 - Exercise 2.12
p = 100
r = .07
n = 10
a = p*(1+r) ** n
print ('After 10 years: $',a)
p = a
b = p * (1 +r) ** n
print('After 20 years: $',b)
p = b 
c = p * (1+r) ** n
print('After 30 years: $',c)

