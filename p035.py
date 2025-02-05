# Circular Primes

from eulerlib import list_primes, is_prime
from collections import deque

def circular_primes(n = 1_000_000):
    total = 0
    for prime in list_primes(n):
        if set(str(prime)) & set("02468"): continue
        nums = (get_rotations(deque(str(prime))))                       
        if all((is_prime(int(''.join(num))) for num in nums)):
            total += 1
    return total

def get_rotations(n: deque):
    for _ in range(len(n)):
        n.rotate()
        yield n

def compute():
    return str(circular_primes())

import time
if __name__ == "__main__":
    timer = time.time()
    print(compute())
    print(f"Elapsed: {(time.time() - timer)*1000:.3f} ms")
