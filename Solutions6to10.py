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


# Problem 7. Find the 10,001st prime.
# Commented out because the code isn't very efficient. Not sure how to speed it up

# PrimeList = [2,3]
# x = 5
# PrimesChecked = 0
# while len(PrimeList) <= 10001:
#     for p in PrimeList:
#         if x%p != 0:
#             PrimesChecked += 1
#     if PrimesChecked == len(PrimeList):
#         PrimeList.append(x)
#     PrimesChecked = 0
#     x+=2

# print("Solution 7: ",PrimeList[10000])
        

# Problem 8. Weird adjacency problem.. :| Hwat? 13 adjacent digits with largest
# Product. Return the actual product.

GodInt = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
LargestProduct = 2000
ValueList = []
product = 1
for i in range(988):
    for j in range(i,i+13):
        product *= int(str(GodInt)[j])
    if product > LargestProduct:
        LargestProduct = product
    product = 1
        
print("Solution 8: ",LargestProduct)
    
# Problem 9. Find product of values in Pythagorean triplet
# of 1000.
import math
TestVal = 0
FinalVal = 0
for a in range(1,1000):
    for b in range(1,1000):
        csq = a*a + b*b
        if int(math.sqrt(csq)) == math.sqrt(csq):
            TestVal = a + b + math.sqrt(csq)
        if a + b + math.sqrt(csq) == 1000:
            FinalVal = a*b*math.sqrt(csq)
print("Solution 9: ",FinalVal)

# Problem 10. Sum of all primes below 2 million.

# PrimeList2 = [2,3]
# x = 5
# PrimesChecked = 0
# while PrimeList2[-1] <= 2000000:
#     for p in PrimeList2:
#         if x%p != 0:
#             PrimesChecked += 1
#     if PrimesChecked == len(PrimeList2):
#         PrimeList2.append(x)
#     PrimesChecked = 0
#     x+=2

# print("Solution 10: ",sum(PrimeList2))
# This uses the the Sieve of Erastothenes to find primes more efficiently.
# Note, I used the algorithm on Wikipedia to start but I still had some issues
# and eventually made a few small alterations (e.g. forgot to add BoolList[0]=False or
# BoolList[1] = False. I found a solution that was structurally similar to my code)

n = 2000000
BoolList = [True]*n
NumbList = list(range(n))
step = 2
BoolList[0]= False
BoolList[1]= False
while step*step < n:
    if BoolList[step] == True:
        for j in range(step*2, n, step):
            #print(j)
            BoolList[j] = False
       
    step+=1

#print(BoolList)
SumOfPrimes = 0
for x in range(n): 
        if BoolList[x]: 
            SumOfPrimes += x
            
print("Solution 10: ",SumOfPrimes)
    

