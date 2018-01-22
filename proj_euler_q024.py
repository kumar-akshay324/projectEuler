# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

num_set = [0,1,2,3,4,5,6,7,8,9]


# number_index = 0
# for i in num_set:
#     number_index += 9**9
#     if number_index>1000000000:
#         break

num_list = list(itertools.permutations(num_set))

str_number = ''
for digit in num_list[999999]:
    str_number = str_number + str(digit)
    # print (digit)

print ("Millionth number is %d" %(int(str_number)))





