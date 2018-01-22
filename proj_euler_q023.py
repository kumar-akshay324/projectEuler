# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import numpy as np

abundant, sum_list = [], []
final_summ = 0
for i in range(1, 28124):
    summ = 0
    for j in range(1, int(i/2 + 1)):
        if i%j==0:
            summ+=j
    if summ>i:
        abundant.append(i)

number_list = [num for num in range(1,28124)]
for p in abundant:
    for q in abundant:
        if (p+q)<28124:
            sum_list.append(p+q)

final_summ = np.sum(np.asarray(list(set(number_list) - set(sum_list))))

# divisorsum = [0]*LIMIT
# for i in range(1, LIMIT):
#     for j in range(i * 2, LIMIT, i):
#         divisorsum[j] += i
# abundantnums = [i for (i, x) in enumerate(divisorsum) if x > i]

# print(abundant)
print ("Final sum of numbers that cannot be written as a sum of two abundant numbers is %d " %(final_summ))

