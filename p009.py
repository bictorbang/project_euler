# Special Pythagorean Triplet


def special_pythagorean_triplet(n = 1_000):
    threshold = n // 3 - 1
    for a in range(1, threshold):
        b = a + 1
        c = n - a - b
        while c > b:
            if a*a + b*b == c*c:
                return a*b*c
            b += 1
            c -= 1
    return -1

def compute():
    return str(special_pythagorean_triplet())

if __name__ == "__main__":
    print(compute())
