nums_str = [] 
single_str = ''

nums_str.append("73167176531330624919225119674426574742355349194934")
nums_str.append("96983520312774506326239578318016984801869478851843")
nums_str.append("85861560789112949495459501737958331952853208805511")
nums_str.append('12540698747158523863050715693290963295227443043557')
nums_str.append('66896648950445244523161731856403098711121722383113')
nums_str.append('62229893423380308135336276614282806444486645238749')
nums_str.append('30358907296290491560440772390713810515859307960866')
nums_str.append('70172427121883998797908792274921901699720888093776')
nums_str.append('65727333001053367881220235421809751254540594752243')
nums_str.append('52584907711670556013604839586446706324415722155397')
nums_str.append('53697817977846174064955149290862569321978468622482')
nums_str.append('83972241375657056057490261407972968652414535100474')
nums_str.append('82166370484403199890008895243450658541227588666881')
nums_str.append('16427171479924442928230863465674813919123162824586')
nums_str.append('17866458359124566529476545682848912883142607690042')
nums_str.append('24219022671055626321111109370544217506941658960408')
nums_str.append('07198403850962455444362981230987879927244284909188')
nums_str.append('84580156166097919133875499200524063689912560717606')
nums_str.append('05886116467109405077541002256983155200055935729725')
nums_str.append('71636269561882670428252483600823257530420752963450')

maxx = 0
for s in range(1,21):
	single_str = single_str + nums_str[s-1]
for i in range(1,988):
	summ = int(single_str[i])*int(single_str[i+1])*int(single_str[i+2])*int(single_str[i+3])*int(single_str[i+4])*int(single_str[i+5])*int(single_str[i+6])*int(single_str[i+7])*int(single_str[i+8])*int(single_str[i+9])*int(single_str[i+10])*int(single_str[i+11])*int(single_str[i+12]) 
	if maxx<summ:
		maxx = summ
		maxx_index = i
print ("Maximum sum is %d \n \n " %(maxx))
# print ("Values are %d %d %d %d %d %d %d %d %d %d %d %d %d " %(int(single_str[maxx_index]),int(single_str[maxx_index+1]),int(single_str[maxx_index+2]),int(single_str[maxx_index+3]),int(single_str[maxx_index+4]),int(single_str[maxx_index+5]),int(single_str[maxx_index+6]),int(single_str[maxx_index+7]),int(single_str[maxx_index+8]),int(single_str[maxx_index+9]) + int(single_str[maxx_index+10]),int(single_str[maxx_index+11]),int(single_str[maxx_index+12])))
print ("Maximum product is at index %d and starts with the value %d" %(maxx_index+1, int(single_str[maxx_index+1])))