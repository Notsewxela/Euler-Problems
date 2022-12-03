'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import numpy as np

def sieve_of_eratosthenes(n):

    n = int(n)
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
        
    prime.pop(0) #0 is not a prime
    prime.pop(0) # 1 is not a prime
    primes = np.arange(2, n+1)
    primes[np.logical_not(prime)] = 0 #set all non primes to 0
    
    
    return primes[primes.nonzero()] #return only non-zero values (we zeroed the non-primes!)

print(np.sum(sieve_of_eratosthenes(2e6)))
