'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

# As with previous problem, can "cheat" with python autobigint stuff

import numpy as np

# Calcs the number of digits in m!, m is integer
def digit_tot(m): # m >= 1
    if m == 1:
        return 1
    return int(np.ceil(np.sum(np.log10(np.arange(1, m+1)))))

def factorial(n):
    '''Returns an array of the digits of n factorial'''
    digits = np.zeros(digit_tot(n), dtype=np.int16)
    # 1! = 1. Digits are stored in reverse order and then flipped at the end!
    digits[0] = 1
    for factor in range(2, n+1):
        carry = 0
        for i in range(len(digits)):
            digits[i] = digits[i] * factor + carry
            if digits[i] >= 10:
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                carry = 0
        i=0
        while carry != 0:
            digits[i] = carry % 10
            carry /= 10
            i += 1
    return np.flip(digits)

n = 100
print(np.sum(factorial(n)))