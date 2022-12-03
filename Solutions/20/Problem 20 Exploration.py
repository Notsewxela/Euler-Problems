'''
Want to plot the function as a factor of n and my code slow because no memoization
'''

import matplotlib.pyplot as plt
import math

def fac_sum(n):
    a = list(str(math.factorial(n)))
    return sum([int(x) for x in a])


lim = 10000

y = [fac_sum(p) for p in range(1, lim)]

plt.plot(range(1, lim), y)
plt.xlabel("$n$", fontsize = 14)
plt.ylabel("Sum of the digits of $n!$", fontsize = 14)
plt.show()