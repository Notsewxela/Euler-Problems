'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import numpy as np
import matplotlib.pyplot as plt

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

def calc_smallest(n):
    vals = prods(n)
    for x in range(n**2):
        try:
            ab, a, b = next(vals)
        except StopIteration:
            break
        #print(ab, a, b)
        if palindrome(ab):
            print(f"The largest palindrome that is the produt of two 3-digit numbers is {ab} = {a} x {b}")
            break

#do euler probem
n=999
calc_smallest(n)