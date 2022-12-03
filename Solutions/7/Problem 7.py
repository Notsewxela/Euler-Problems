'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def get_nth_prime(nth):
  """ Returns the n-th prime number
  """
  total_primes = 0
  size_factor = 2
  s = (nth * size_factor)
  while total_primes < nth:
    primes = get_primes(s)
    total_primes = sum(primes[2:])
    size_factor += 1
    s = (nth * size_factor)
  nth_prime = count_primes(primes, nth)
  return nth_prime


def get_primes(s):
  """ Generates primes using the Sieve of Eratosthenes
      Includes the optimization where for every prime p, only factors p >= p^2
      are verified.
      The list of primes is represented with a bytearray. Each index corresponds
      to an integer in the list. A value of "1" at the index location indicates
      the integer is a prime.
  """
  primes = bytearray([1]*s)
  for i in range(2, s):
      if primes[i] == 1:
        for j in range(i, s):
          if i*j < s:
            primes[i*j] = 0
          else:
            break
  return primes


def count_primes(primes, nth):
  """ Returns the n-th prime represented by the index of the n-th "1" in the
      bytearray.
  """
  count = 0
  for k in range(2, len(primes)):
    count += primes[k]
    if count == nth:
      return k

# Get the nth prime number
N_TH = 10001
nth_prime = get_nth_prime(N_TH)
print("The {}-th prime is: {}".format(N_TH, nth_prime))