# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75

# 95 64
# 17 47 82

# 18 35 87 10
# 20 04 82 47 65

# 19 01 23 75 03 34
# 88 02 77 73 07 63 67

# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33

# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14

# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48

# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

numArray = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

partialSumArray, partialSumArray2, partialSumArray3, partialSumArrayfinal =[], [], [], []
# arr1 = [numArray[0][0] +  numArray[1][0], numArray[0][0] +  numArray[1][1]]
# partialSumArray.append(arr1)

for p in range(14,0,-2):

    sumpart1  = [numArray[p][i] + numArray[p-1][i] for i in range(0,len(numArray[p-1]))]
    sumpart2  = [numArray[p][i+1] + numArray[p-1][i] for i in range(0,len(numArray[p-1]))]
    summ = sumpart1 +  sumpart2
    partialSumArray.append(summ)
partialSumArray = numArray[0] + partialSumArray
print (len(partialSumArray))


# for p in range(7,-1,-2):
p = 7
sumpart1  = [partialSumArray[p][i] + partialSumArray[p-1][i] for i in range(0,len(partialSumArray[p-1]))]
sumpart2  = [partialSumArray[p][i+1] + partialSumArray[p-1][i] for i in range(0,len(partialSumArray[p-1]))]
summ = sumpart1 + sumpart2
partialSumArray2.append(summ)

partialSumArray2 = numArray[0] + partialSumArray
print (len(partialSumArray))



sum = numArray[0][0] + numArray[p][i] + numArray[p][i]   





# for q in range(0,6,2):
#     spart1 = [partialSumArray[q][i] + partialSumArray[q + 1][i + 1] for i in range(0, len(partialSumArray[q]))]
#     spart2 = [partialSumArray[q][i] + partialSumArray[q + 1][i] for i in range(0, len(partialSumArray[q]))]
#     sm = spart1 + spart2
#     partialSumArray2.append(sm)
#
# spart1 = [partialSumArray[6][i] + partialSumArray[q + 1][i + 1] for i in range(0, len(partialSumArray[q]))]
# spart2 = [partialSumArray[q][i] + partialSumArray[q + 1][i] for i in range(0, len(partialSumArray[q]))]
# sm = spart1 + spart2
# partialSumArray2.append(sm)



# for r in range(0,4,2):
#
#     sspart1 = [partialSumArray2[r][i] + partialSumArray2[r + 1][i + 1] for i in range(0, len(partialSumArray2[r]))]
#     sspart2 = [partialSumArray2[r][i] + partialSumArray2[r + 1][i] for i in range(0, len(partialSumArray2[r]))]
#     smm = sspart1 + sspart2
#     partialSumArray3.append(smm)
#
#
# finalpart1 = [partialSumArray3[0][i] + partialSumArray3[1][i + 1] for i in range(0, len(partialSumArray3[0]))]
# finalpart2 = [partialSumArray3[0][i] + partialSumArray3[1][i] for i in range(0, len(partialSumArray3[0]))]
# smmfinal = finalpart1 + finalpart2
# partialSumArrayfinal.append(smmfinal)


# print (partialSumArray)
# print (len(partialSumArrayfinal))


