'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

import numpy as np

upper = 1000

x = np.arange(1, upper + 1)
y3 = x % 3
y5 = x % 5

print(np.sum(x[(y3==0) | (y5==0)]))