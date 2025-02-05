# Factorial Digit Sum

from math import factorial

def factorial_digit_sum(n = 100):
    return sum((int(d) for d in str(factorial(n))))

def compute():
    return str(factorial_digit_sum())
    
if __name__ == "__main__":
    print(compute())
