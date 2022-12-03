'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import numpy as np

#does the descending products below n**2 in correct order
def prods(n):
    diff = 0
    while diff < n:
        ridge = int(np.ceil(diff/2))
        a, b = ridge, diff-ridge
        yield (n-a)*(n-b), n-a, n-b
        b -= 1
        while (b >= 0):
            a += 1
            yield (n-a)*(n-b), n-a, n-b
            b -= 1
        diff += 1

def palindrome(y):
    y = str(y)
    if y == y[::-1]:
        return True
    else:
        return False

def calc_max_val_from_digits(digits):
    val = ""
    for i in range(digits):
        val += "9"
    return int(val)

def calc_smallest(digits):
    n = calc_max_val_from_digits(digits)
    vals = prods(n)
    for x in range(n**2):
        try:
            ab, a, b = next(vals)
        except StopIteration:
            break
        #print(ab, a, b)
        if palindrome(ab):
            print(f"The largest palindrome that is the produt of two {digits}-digit numbers is {ab} = {a} x {b}")
            break

#do euler probem
min_digits = 1 #less than 1 digit doesn't make sense obviously
max_digits = 9 #takes a *very* long time past 8
for digits in range(min_digits, max_digits + 1): 
    calc_smallest(digits)