# # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# # Find the sum of all the primes below two million.

summ, count = 5,0

for i in  range(4,20001):

	if i%2==0 or i%3==0:
		continue

	for j in range(1,i):
		if i%j == 0:
			count = count + 1
			if count >2:
				continue
	summ = summ + j
	count = 0
	# print (i)	
print ("Sum is %d " %(summ))			

# t=[]
# t.append((1,2))
# print t[1]