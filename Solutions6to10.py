# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:27:31 2019

@author: asus
"""

# Sum of squares by square of sums for first 100 natty numbs
SoSq = 0
for i in range(1,101):
    SoSq += i*i

print("SoSq = ",SoSq)

SqoS = 0
for j in range(1,101):
    SqoS += j

SqoS = SqoS*SqoS
print("SqoS = ",SqoS)
    
print("Solution 6: ", SqoS-SoSq)