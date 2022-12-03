'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

# Note, I could cheat and just use python's auto bigint behaviour but that doesn't apply to most languages so i consider it cheating here

import numpy as np

def digits_of_power(power):
    # power is an integer

    #formula accurately tells us how many digits we need
    digits = np.zeros(1+int(np.floor(power*np.log10(2))), dtype=np.int8) #only needs to be int8 to store numbes 0-9
    digits[0] = 1 #2**0 = 1
    
    carry = 0
    for j in range(0, power):
        for i in range(0, len(digits)):
            temp = digits[i] * 2
            if temp >= 10:
                digits[i] = temp - 10 + carry
                carry = 1
            else:
                digits[i] = temp + carry
                carry = 0
    
    return np.sum(digits)

def cheat_digits_of_power(power):
    # a lot faster for big numbers but is cheating!!!
    number = 2**power
    return sum([int(x) for x in str(number)])