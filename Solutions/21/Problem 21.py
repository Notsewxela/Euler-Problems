'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from functools import lru_cache

@lru_cache(maxsize=None)
def proper_divisors(n) -> list:
    '''
    Takes a natural number n and returns a list of its proper divisors (i.e. not including n).
    '''
    divisors = []
    if n == 1: return divisors
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

@lru_cache(maxsize=None)
def d(n) -> int:
    return sum(proper_divisors(n))
    
def amicable_numbers(limit = 10000) -> int:
    # making it a set makes sure we don't double count
    amicables = set()
    for m in range(2, limit + 1):
        n = d(m)
        # d(n) == m is not allowed
        if n == m:
            continue
        # n and m are amicable
        if m == d(n):
            amicables.add(m)
            amicables.add(n)
    return amicables

amicable_numbers()