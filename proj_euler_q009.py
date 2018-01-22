# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
flag = 0

for i in range(1,1001):
	for j in range(1,1001):
		if ((i**2 + j**2)**0.5)%1 ==0 and i+j+math.sqrt(i**2+j**2) ==1000:	
			flag = 1
			break
	if flag ==1:
		break
print ("The product is %d " %(i*j*math.sqrt(i**2 + j**2)))			
