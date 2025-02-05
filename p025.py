# 1000-digit Fibonacci Number
from functools import cache

def n_digit_fibonacci_number(n = 1_000):
    m = 1
    while len(str(fibonacci(m))) < n:
        m += 1
    return m

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def compute():
    return str(n_digit_fibonacci_number())
    
if __name__ == "__main__":
    print(compute())

    