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



#plot the pattern of the values out of interest

vals = prods(n)
pairs = np.zeros((2, n**2))
results = np.zeros(n**2)
for x in range(n**2):
    try:
        ab, a, b = next(vals)
        pairs[0, x] = a
        pairs[1, x] = b
        results[x] = ab
    except StopIteration:
        break

#don't make this value too big or program will crash as not enough memory!
max_plot_pair = 10
plt.scatter(pairs[0, :max_plot_pair], pairs[1, :max_plot_pair], c = results[:max_plot_pair], cmap='plasma')