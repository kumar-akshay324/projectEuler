# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

f_n_1, f_n_2 = 1, 1
done = False
n = 3
while True:

    f_n = f_n_1 + f_n_2
    if len(str(f_n))>=1000:
        break
    f_n_2 = f_n_1
    f_n_1 = f_n
    n+=1

print ("Index of first Fibonacci Series term with more than 1000 digits is %d " %(n))