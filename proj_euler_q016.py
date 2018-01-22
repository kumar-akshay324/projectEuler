# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

import math

# num = math.pow(2,1000)
num = 2**1000
sum = 0

for i in str(num):
    sum += int(i[0])
    # print (i)

# print (str(num)[0])
print ("Sum of digits is %d" %(sum))