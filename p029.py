# Distinct Powers

def distinct_powers(a1 = 2, a2 = 100, b1 = 2, b2 = 100):
    powers = set((a**b for a in range(a1, a2 + 1) for b in range(b1, b2 + 1)))
    return len(powers)


def compute():
    return str(distinct_powers())
    
if __name__ == "__main__":
    print(compute())
