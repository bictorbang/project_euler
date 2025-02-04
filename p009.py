# Special Pythagorean Triplet

import time

def special_pythagorean_triplet(n = 1_000):
    threshold = n // 3 - 1
    for a in range(1, threshold):
        b = a + 1
        c = n - a - b
        while c > b:
            if a*a + b*b == c*c:
                return a*b*c, a, b, c
            b += 1
            c -= 1
    return -1


timer = time.time()
res, a, b, c = special_pythagorean_triplet(5000)
print(f"Result = {res}\nTime elapsed: {time.time() - timer:.6f}s")
print(a, b, c)