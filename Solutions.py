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
        