#Even Fibonacci Numbers

def even_fibonacci_numbers(n = 4_000_000):
    res = 0 
    n_1 = 1
    n_2 = 2
    while n_1 <= n:
        if n_1 % 2 == 0:
            res += n_1
        n_1, n_2 = n_2, n_1 + n_2
    return res

def compute():
    return str(even_fibonacci_numbers())

if __name__ == "__main__":
    print(compute())
