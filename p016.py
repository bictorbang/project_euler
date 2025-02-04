# Power Digit Sum 

def power_digit_sum(N = 2, n = 1000):
    return sum((int(i) for i in str(N**n)))

def compute():
    return str(power_digit_sum())
    
if __name__ == "__main__":
    print(compute())
