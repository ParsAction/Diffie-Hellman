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
def MECalc(j, k, l):
    J = j
    K = k
    Z = 1
    while K > 0:
        if K % 2 == 0:
            J = (J * J) % l
            K = K/2
        else:
            Z = (J * Z) % l
            K = K - 1
    return Z



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
