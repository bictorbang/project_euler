# Smallest Multiple

import math

def smallest_multiple(a = 1, b = 21):
    n = range(a, b)
    return math.lcm(*n)

def compute():
    return str(smallest_multiple())
    
if __name__ == "__main__":
    print(compute())

