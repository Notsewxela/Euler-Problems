import numpy as np
import matplotlib.pyplot as plt

#set the upper limit of our numbers to test wouldn't recommend much above 10000 due to memory implications of a
#square array being so big
upper = 5000
#creates an array of our natural numbers in appropriate range
x = np.arange(1, upper + 1) 

#creates a triangular array of sums of numbers with zeroes in lower left half
#uint16 is to minimise data size
vals = np.uint16(np.repeat(x, upper).reshape(upper, upper))
vals = np.triu(vals)

#creates arrays of our numbers mods 3 and 5
vals3 = vals % 3
vals5 = vals % 5

#sets all values of our 
vals[(vals3!=0) & (vals5!=0)] = 0

#the result! sums as it should
result = np.sum(vals, axis=0)

#output results!
print(result)
plt.plot(x, result, "bx")