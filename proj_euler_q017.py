# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

wordsDictUpTo20 = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
             14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty"}
wordsDictUpTo100 = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

lengthSum = 0

for i in range(1,1001):

    if i<21:
        num2word = wordsDictUpTo20[i]

    if i>20 and i<100:
        num2word = wordsDictUpTo100[int(i/10)] + wordsDictUpTo20[int(i%10)]
    # elif i>20 and i<100 and i%10==0:
    #     num2word = wordsDictUpTo100[int(i/10)]

    if i>99 and i%100!=0 and i!=1000:
        hundrethNum = int(i/100)
        tenthNum = (i - hundrethNum*100 - i%10)/10
        unitNum = i%10

        if tenthNum>1:
            n2w = "and" + wordsDictUpTo100[tenthNum] + wordsDictUpTo20[unitNum]
        elif tenthNum==0:
            n2w =  "and" +  "" + wordsDictUpTo20[unitNum]
        elif tenthNum==1:
            n2w = "and" + wordsDictUpTo20[(i - hundrethNum*100)]
        num2word = wordsDictUpTo20[hundrethNum] + "hundred" +  n2w

    elif i>99 and i%100==0  and i!=1000:
        hundrethNum = int(i/100)
        n2w = ""
        num2word = wordsDictUpTo20[hundrethNum] + "hundred" +  n2w

    if i==1000:
        num2word = "onethousand"

    print (num2word)
    lengthSum += len(num2word)

print ("Total number of letter used %d" %(lengthSum))

