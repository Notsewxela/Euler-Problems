"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from functools import lru_cache

NON_ABUNDANT_NUMBER = 28123 # highest non-abundant integer

@lru_cache(maxsize=None)
def proper_divisors(n):
    divisors = []
    if n == 1: return divisors
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

@lru_cache(maxsize=None)
def calc_abundants(limit=NON_ABUNDANT_NUMBER):
    abundants = []
    for n in range(limit + 1):
        if sum(proper_divisors(n)) > n:
            abundants.append(n)   
    return abundants

def is_abundant_sum(n, abundants=calc_abundants()):
    if n > NON_ABUNDANT_NUMBER: # all integers bigger than this are a sum of two abundant numbers
        return True
    for i in abundants:
        if i > n /2: # if i > n/2 then no possible for an abundant sum
            return False
        if n-i in abundants: # i + n-i = n and i, n-i are both abundants
            return True
    return False

def main():
    non_abundant_total = 0
    for n in range(NON_ABUNDANT_NUMBER + 1):
        if not(is_abundant_sum(n)):
            non_abundant_total += n
    return non_abundant_total