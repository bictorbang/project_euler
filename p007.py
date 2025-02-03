# 10 001st Prime

from eulerlib import is_prime

def nth_prime(n = 10_001):
    primes = [2]
    i  = 3
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return primes[-1]

def compute():
    return str(nth_prime())

if __name__ == "__main__":
    print(compute())

