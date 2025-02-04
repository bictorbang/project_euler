# Summation of primes

from eulerlib import list_primes # , is_prime

'''
def summation_of_primes(n = 2_000_000):
    primes = [2]
    i  = 3
    while i < n:
        if is_prime(i):
            primes.append(i)
        i += 2
    return sum(primes)
'''

def summation_of_primes(n = 2_000_000):
    return sum(list_primes(n))

def compute():
    return str(summation_of_primes())

if __name__ == "__main__":
    print(compute())
