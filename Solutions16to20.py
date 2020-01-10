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