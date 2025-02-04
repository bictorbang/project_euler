# Highly Divisible Triangular Number

from math import prod #, sqrt
from itertools import count
from collections import Counter

# Credits to Mikhail Lomonosov
def highly_divisible_triangular_number(n = 500):
    precomputed = 10**5
    primes = smallest_prime(precomputed)

    def factorint(n1, primes = primes):
        factors = Counter()
        while n1 > 1:
            if n1 > precomputed:
                for p in range(2, precomputed + 1):
                    if primes[p] != p: continue
                    if n1 % p == 0: break
            else: p = primes[n1]
            factors[p] += 1
            n1 //= p
        return factors

    triangle_numbers = (n * (n + 1) // 2 for n in count(1))
    for t in triangle_numbers:
        if prod(m + 1 for m in factorint(t).values()) > n: return t

def smallest_prime(n):
    primes = list(range(n + 1))
    for p in range(2, n + 1):
        if primes[p] == p:
            for i in range(p*p, n + 1, p):
                primes[i] = p
    return primes


'''
# Not very fast (around 3s)
def highly_divisible_triangular_number2(n = 500):
    m = 1
    i = 2
    while len(list(divisorGenerator(m))) <= n:
        m += i
        i += 1
    return m

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
'''

def compute():
    return str(highly_divisible_triangular_number())
    
if __name__ == "__main__":
    print(compute())
