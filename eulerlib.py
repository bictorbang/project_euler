import math

def is_prime(n):
    if n <= 1 : return False
    if n < 4: return True
    if n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False

    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True

# Crible d'Ératosthène
# [False, False, True, True, False, True, False, True, ...]
def list_primality(n):
    primes = [True] * (n + 1)
    primes[0] = primes [1] = False
    for i in range(math.isqrt(n) + 1):
        if primes[i]:
            for j in range(i*i, len(primes), i):
                primes[j] = False
    return primes

# Renvoie la liste des nombres premiers inférieurs à n
# [2, 3, 5, 7, 11, 13, 17, 19, 23, ...]
def list_primes(n):
    return [i for (i, prime) in enumerate(list_primality(n)) if prime]