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

print("Solution to 16: ",summation)


# Problem 17
# Hwat? This is definitely not something I have ever encountered lol XD
# At a minimum, I'd have to manually count every digit to 19, then 20 to 90
# count by tens. Then 100 - 1000 count by 100s. That'll be my "bag of words"
# to combine.
# E.g., for 1234 I have One Thousand (from the count by 100s) Two Hundred 
# (from the count by 100s) and Thirty (from the count by 10s) four (count by 1's)
# Though I needn't consider 1000's. I can just count manually and add it.
# I lied, a bit of a pattern appears at 16.

# This isn't my favorite problem..I don't see it as being smart to program it..
summationTo99 = 36 + 70 + 10*(6 + 6 + 5 + + 5 + 5 + 7 + 6 + 6) + 8*36
print(summationTo99)

# 1 - 99 has 854 letters.
# 100 - 900 mod 10 has 36 + 7 * 9 = 63 letters
# 101 - 999: one hundred and appears 890 times: from 999 - 100 - 8 (because we omitted 100 so we subtract 8 instead of 9)

solution = 891*10 + 63 + 3600 + 9*854 + 11 + 854

print("Solution to 17: ",solution)


# Problem 18
# Note, for reading the matrix in I kind of took a lazy approach. I prepped the
# data in excel via: Copy from Proj Euler > Paste into Excel > highlight data
# (since it appears in one column) > Data > Text to Columns > delimit by Space
# > Find and Replace empty cells with zeros.
# This creates a 'right-triangle' of the data rather than the way it is shown
# online. But it's the same idea. Just that it can go down or down-right.
import numpy as np
matrix = np.loadtxt("MatrixReadInForProblem18.txt",delimiter='\t')

# Not sure entirely how to implement the brute force given the structure of the data
# But I can try working my way up. Rather than down and down-right, I would go up
# and up-left. If I choose the max of those, it should return the max since we ended
# there anyways..

# =============================================================================
# TotalSum = 0
# MaxSum = 2
# for StartColumn in range(14,-1,-1):
#     CurrentColumn = StartColumn
#     TotalSum = matrix[14][StartColumn]
#     
#     for i in range(13,-1,-1):
#         if matrix[i][CurrentColumn] > matrix[i][CurrentColumn-1]:
#             TotalSum += matrix[i][CurrentColumn]
#         else:
#             TotalSum += matrix[i][CurrentColumn-1]
#             CurrentColumn -= 1
#         
#         if StartColumn == 3:
#             print("matrix[",i,"][",CurrentColumn,"]"," = ", matrix[i,CurrentColumn])
#             print("Total Sum: ",TotalSum)
#         #if StartColumn == 4:
#             # print("Value above: ",matrix[i][CurrentColumn]," | Values Up-left: ",matrix[i][CurrentColumn-1])
#         # print("Total Sum in row ",i," = ",TotalSum, " || Starting Column: ",StartColumn)
#     #print(TotalSum, " for start value of ", matrix[14][StartColumn])
#     if TotalSum > MaxSum:
#         MaxSum = TotalSum
#         
# print("Solution to Problem 18: ", MaxSum)
# =============================================================================
    
# =============================================================================
# So the above was my attempt at coding this but my approach isn't accurate.
# I think I might be missing higher values but always choosing the largest of
# two choices. I did, however, find an algorithm that might work better though
# I'm still unsure of how much it differs from my approach.
# Logically it should yield the same result but perhaps with higher efficiency
# =============================================================================
    
# Note: I authored the below code but I had to look up this approach. I didn't
# independently discover this algorithm. But it is a very clean and intelligent
# approach!

for row in range(13,-1,-1):
    for col in range(14):
        matrix[row,col] = matrix[row,col] + max(matrix[row+1,col],matrix[row+1][col+1])
        
print("Solution to Problem 18: ",matrix[0,0])
    

# Problem 19
# Hope this isn't cheating lol. But there's a library for this
# already so I don't have to build a bunch of conditionals.
# Otherwise I'd need some conditionals to deal with the different days per month

from datetime import date
SundayCounter = 0
for year in range(1901,2001):
    for month in range(1,13):
        if date(year,month,1).weekday() == 6:
            SundayCounter+=1
                    

print("Solution to Problem 19: ",SundayCounter)

# Problem 20
# Factorial Digit Sum
# This one's not too tough. Just calculate the factorial (Note: by 1M it takes a few seconds)
# Then use the list property that converts a string into individual entries by letters in the string.
# Convert those to ints and sum! :)

factorial = 1
for i in range(100,0,-1):
    factorial *= i
    
factorialList = list(str(factorial))
summation = 0
factorialList = [int(x) for x in factorialList]
for digit in factorialList:
    summation += digit

print("Solution to problem 20: ",summation)

    
    