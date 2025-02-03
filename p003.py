# Largest Prime Factor

def largest_prime_factor(n = 600_851_475_143):
    for k in range(2, n + 1):
        while n % k == 0: n //= k
        if n == 1: return k 

def compute():
    return str(largest_prime_factor())

if __name__ == "__main__":
    print(compute())