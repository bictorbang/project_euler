# Multiples of 3 or 5 

def multiples_of_a_or_b(n = 1000, a = 3, b = 5):
    return sum((i for i in range(n) if (i%a == 0 or i%b == 0)))

def compute():
    return str(multiples_of_a_or_b())

if __name__ == "__main__":
    print(compute())