# The sum of the squares of the first ten natural numbers is a 
# The square of the sum of the first ten natural numbers is b
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is b-a
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
summ, sq_sum = 0, 0
for i in range(1,101):
	summ = summ + i
	sq_sum = sq_sum + i**2
diff = 	summ**2 - sq_sum
print ("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum %d " %(diff))