# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import numpy as np
num, factor, flag = 20, 0, 0
li = [20,19,18,17,16,15,14,13,12,11,10,3]
while flag!=1:
	for i, div in enumerate(li):
		if num%(i+1) ==0 and (num/(i+1))%2 ==0:
			factor = factor + 1
		else:
			break
	if factor==20:
		flag =1
	num = num + 1
	factor =0	
print ("Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is %d" %(num-1))
		




