# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

n,c,n_count=1,0,0

while True:
	for i in range(1,n+1):
		if n%i ==0:
			c = c +1
	if n==2:
		n_count = n_count +1
	if n_count == 10001:
		break
	n = n + 1	
print ("The 10 001st prime number is %d" %(n))
		

			