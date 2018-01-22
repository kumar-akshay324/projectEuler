# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import numpy as np
divSum = [1,1]
amicableSum = 0
pair1, pair2 = [], []

for i in range(2, 10000):
    divisors = []

    for j in range(1,int(i/2 + 1) ):
        if i%j==0:
            divisors.append(j)
    # print (divisors)
    divSum.append(int(np.sum(np.asarray(divisors))))
# print (divSum)
# print (divSum.index(284))

for p in range(1,10000):

    if divSum[p]<10000:
        if p == divSum[divSum[p]] and p!=divSum[p]:
            # pairr = tuple((p, divSum[p]))
            # if pairr not in pairs:
            #     pairs.append(pairr)
            pair1.append(p)
            pair2.append(divSum[p])
            amicableSum += (p + divSum[p])
            print ("Pairs are %d , %d " %(p, divSum[p]))
print (pair1)
print (pair2)
print ("Sum of amicable numbers below 10000 is %d" %(sum(pair1)))
# print (divSum)
