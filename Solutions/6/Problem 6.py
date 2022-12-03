'''The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

import numpy as np

n=100
vals = np.arange(1,n+1)

sq_of_sum = np.sum(vals)**2
sum_of_sq = np.sum(vals*vals)

print(sq_of_sum-sum_of_sq)