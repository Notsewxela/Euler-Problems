'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
#calculates the prime factors of an integer by:
#if number divides the integer divide out that factor
#keep going until the function finds a number that doesnt divide and
#increment the test factor to find the next one that divides and repeat
#is O(n) worst case (prime number)
#note the function repeats repeated factors. e.g. 16 is 2 2 2 2 rather than just 2
def prime_factors(input_val):
    factors = []
    n = input_val
    c = 2
    while n > 1:
        if n % c == 0:
            factors.append(c)
            n /= c
        else:
            c += 1
    return factors

target = 600851475143
print(prime_factors(target))