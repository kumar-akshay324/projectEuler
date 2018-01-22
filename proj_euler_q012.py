# What is the value of the first triangle number to have over five hundred divisors?

n, tri_temp, i, factors = 0, 0, 1, 0

while True:

	tri = tri_temp + i

	for i in range(1,tri):
		if tri%i ==0:
			factors+=1
	i+=1
	if factors>500:
		break
	factors = 0
	tri_temp = tri	

print ("Value of triangle number is" %(tri))	
