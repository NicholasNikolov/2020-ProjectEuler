# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:24:35 2019

@author: asus
"""

# Problem 11. Greatest product of 4 adj numbers.
# Admittedly, this one is a bit tougher for me..
# I'm certain there's a more proper way to approach this.


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

print(max(MatrixOfProducts))