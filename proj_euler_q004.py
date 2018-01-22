# A palindrominc number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009
# Find the largest palindrome made from the product of two 3 digit numbers
numbers =[]
maxx, flag = 0, 0

for i in range(1,1000):
	for j in range(1,1000):
		numbers.append(i*j)

# Checking for palindrome
for ii, num in enumerate(numbers):
	num_str = str(num)
	len_str = len(num_str)
	if len_str%2 ==0:
		len_s = len_str/2
	else:
		len_s = int(len_str/2)
	for pp in range(0, len_s):
		if num_str[pp] != num_str[len_str-1 - pp]:
			flag =1
	if flag !=1:
		if maxx<num:
			maxx = num	
	flag =0	
print ("The largest palindrome from product of two 3-digit numbers is %d" %(maxx))	









