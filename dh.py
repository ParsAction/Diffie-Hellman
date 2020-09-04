#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calc diffie hellman in python for little number
input(g,p,a,b)
A = (g**a) % p
B = (g**b) % p
keyA=(B**a) % p
keyB=(A**b) % p
"""

 

# Modular exponentiation --> A^B mod C = ( (A mod C)^B ) mod C


#Modular Exponentiation Calculation 
def MECalc(x, y, p):
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res



# data entry
g = int(input('input g: '))
p = int(input('input p: '))
a = int(input('input a: '))
b = int(input('input b: '))

print ('')

# Calc A, B
A = MECalc(g, a, p)
B = MECalc(g, b, p)


keyA = MECalc(B, a, p)
print('keyA is: ', keyA)
keyB = MECalc(A, b, p)
print('keyB is: ', keyB)
