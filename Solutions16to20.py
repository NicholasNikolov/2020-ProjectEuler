# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:38:03 2020

@author: asus
"""

# Problem 16
# Find the sum of the digits of 2^1000

x = 2**1000
summation = 0
LengthOfPower = len(str(x))
for i in range(LengthOfPower):
    digit_string = str(x)[i]
    summation += int(digit_string)

print(summation)
