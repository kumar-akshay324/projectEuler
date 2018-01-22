# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Jan = 1, Feb = 2, Mar = 3, Apr =  4, May = 5, June = 6, July = 7, Aug = 8, Sept = 9, Oct = 10, Nov = 11, Dec = 12


import numpy as np

month30 = [4,6,9,11]
month31 = [1,3,5,7,8,10,12]
daysToAdd, daysSum, counter = 0, 0, 0

dateNumtoDay = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
dayOne1901 = 365%7 + 1

for i in range(1901, 2001):
    if (i%4==0) and (i%400==0 or i%100!=0):
        leap = True
    else:
        leap = False

    for j in range(1,13):
        if j in month30:
            daysToAdd = 30
        elif j in month31:
            daysToAdd = 31
        elif j==2 and leap== False:
            daysToAdd = 28
        elif j==2 and leap==True:
            daysToAdd = 29

        daysSum += daysToAdd
        keyWord = daysSum%7 + 1 + dayOne1901

        if keyWord>7:
            keyWord = keyWord - 7
        dayOnFirstDate  =  dateNumtoDay[keyWord]

        if dayOnFirstDate == "Sunday":
            counter+= 1

print ("Number of months in the twentieth century with Sunday as the first date are %d" %(counter))
