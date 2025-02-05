# Quadratic Primes

from itertools import count, takewhile
from more_itertools import ilen
from eulerlib import is_prime, list_primes

# More efficient using range criterias and itertools. (0.4s)
def quadratic_primes(n = 1_000, m = 1_000):
    max_primes = 0
    product = 0
    for b in list_primes(m):
        for a in range(-b + 2, n, 2):
            quad = (i*i + a*i + b for i in count())
            cur = ilen(takewhile(is_prime, quad))
            if cur > max_primes:
                max_primes = cur
                product = a*b
    return product
    
'''
# Bruteforcing here also works. (2.2s)
def quadratic_primes2(n = 1_000, m = 1_000):
    max_primes = 0
    product = 0
    for a in range(-n, n):
        for b in range(m):
            cur = 0
            quad = (i*i + a*i + b for i in count())
            while is_prime(next(quad)):
                cur += 1
            if cur > max_primes:
                max_primes = cur
                product = a*b
    return product
'''

def compute():
    return str(quadratic_primes())
    
if __name__ == "__main__":
    print(compute())
