# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:24:35 2019

@author: asus
"""

# Problem 11. Greatest product of 4 adj numbers.
# Admittedly, this one is a bit tougher for me..
# I'm certain there's a more proper way to approach this.
# NOTE NOTE NOTE!!! This is a super naive approach. If I were to redo this
# I would have one set of nested row and column indexing for-loops and would
# have 4 separate loops within to get products for k. E.g.,
# Row: [i,k+k]
# Column [i+k,j]
# Neg Diag: [i-k,j+k]
# Pos Diag: [i+k,j+k]

# My brain is tired :| Don't judge me!


import numpy as np
M = np.loadtxt('MatrixReadInForProblem11.txt',dtype='i',delimiter=' ')
MatrixOfProducts = []
Product = 1
LargestProductc = 1

for i in range(20):
    for j in range(16):
        for k in range(4):
            Product *= M[i,j+k]
        if Product > LargestProductc:
            LargestProductc = Product
        Product = 1
print("Largest Row Product:" ,LargestProductc)
MatrixOfProducts.append(LargestProductc)
Product = 1
LargestProductr = 1

for j in range(20):
    for i in range(16):
        for k in range(4):
            Product *= M[i+k,j]
        if Product > LargestProductr:
            LargestProductr = Product
        Product = 1        

print("Largest Col Product: ",LargestProductr)
MatrixOfProducts.append(LargestProductr)
Product = 1
LargestProductd1 = 1

for i in range(0,17):
    for j in range(0,17):
        for k in range(4):
            Product *= M[i+k,j+k]
        if Product > LargestProductd1:
            LargestProductd1 = Product
        Product = 1
        
print("Largest Product neg diag: ",LargestProductd1)
MatrixOfProducts.append(LargestProductd1)
Product = 1
LargestProductd2 = 1

for i in range(3,20):
    for j in range(0,17):
        for k in range(4):
            Product *= M[i-k,j+k]
        if Product > LargestProductd2:
            LargestProductd2 = Product
        Product = 1
        
print("Largest Product pos diag: ",LargestProductd2)
MatrixOfProducts.append(LargestProductd2)

print("Solution to Problem 11: ",max(MatrixOfProducts))

# Problem 12
# The nth triangle number is the sum 1 + 2 + ... + n
# Find the first triangle number with over 500 divisors

TriNumb = 0
MaxDivisors = 2
n = 1
DivisorCount = 0
import math

while MaxDivisors < 500:
    # for i in range(1,n+1):
    #    TriNumb += i
    TriNumb = n*(n+1)/2
    
    for j in range(1,int(math.sqrt(TriNumb+1))):
        if TriNumb%j == 0:
            DivisorCount += 2
    
    if DivisorCount >= 500:
        print("Solution to Problem 12: ",TriNumb)
        break;
    
    # if DivisorCount > MaxDivisors:
    #    MaxDivisors = DivisorCount
    
    DivisorCount = 0
    TriNumb = 0
    n += 1
    
    
    
    
    
    