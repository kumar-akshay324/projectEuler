# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
count, maxx =  0, 0
rr = int((num + 1)/2)
for i in range(1,rr):

	if num%i ==0:
		for j in range(1,i+1):
			if i%j== 0:
				count = count + 1

		if count !=2:
			continue
		else:
			if maxx < i:
				maxx = i
print ("Largest Prime factor of the number 600851475143 is %d", maxx)
			





