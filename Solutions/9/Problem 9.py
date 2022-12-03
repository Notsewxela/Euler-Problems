'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


from math import isqrt, gcd

def triplets(N):
    #calcs all pythagorean triplets in NlogN time less than or equal to N
    for m in range(isqrt(N-1)+1):
        for n in range(1+m%2, min(m, isqrt(N-m*m)+1), 2):
            if gcd(m, n) > 1:
                continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            for k in range(1, N//c+1):
                yield k*a, k*b, k*c

def prod(*args):
    product = 1
    for j in args:
        product *= j
    return product

limit = 1000
pythagorean_trip_gen = triplets(limit)

test_val = 1000

while True:
    try:
        vals = next(pythagorean_trip_gen)
        if sum(vals) == test_val:
            product = prod(*vals)
            print(f"{vals} have a sum of {test_val} and a product of {product}")
    except StopIteration:
        break