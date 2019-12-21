# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:48:48 2019

@author: asus
"""

# Find the sum of natural numbers divisible by 3 or 5 less than 1000
x = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 ==0:
        x += i

print("Problem 1: " , x)

# Find sum of even-valued terms in Fibonacci sequence
# whose values do not exceed four million.

first = 1
second = 2
fib = [1,2]
appendVal = 0
while appendVal < 4000000:
    appendVal = first + second
    fib.append(appendVal)
    first = second
    second = appendVal

SumOfEvens = 0

for i in fib:
    if i%2 == 0:
        SumOfEvens += i

print("Problem 2: " , SumOfEvens)
        

# Find the prime factorization of 600851475143

composite = 600851475143
p = 2
factorization = []

while composite >= p:
    if composite%p == 0:
        factorization.append(p)
        composite /= p
    else:
        p += 1
        
print(factorization)

# Find the largest palindromic number made from the
# product of two 3-digit numbers


largestPally = 9009
for i in range(999,100,-1):
    for j in range(999,100,-1):
        pally = i*j
        if str(pally) == str(pally)[::-1]:
            if pally > largestPally:
                largestPally = pally

print("Largest Pally: ",largestPally)

# Smallest positive number that is evenly divisible by all
# number from 1 to 20
# Note. This is the first problem to take a few seconds to
# solve. Therefore there may be grounds for efficiency improvements

condition = False
smallestNumb = 20
while condition == False:
    tester = 0
    for i in range(1,21):
        if smallestNumb %i == 0:
            tester += 1
    if tester == 20:
        condition = True
        break
    smallestNumb += 20
    
print("Problem 5: ",smallestNumb)
    
    
    
    
    


