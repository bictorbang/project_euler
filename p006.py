# Sum Square Difference

def sum_square_difference(n = 100):
    return n*(n-1)*(n+1)*(3*n+2)//12

def compute():
    return str(sum_square_difference())
    
if __name__ == "__main__":
    print(compute())

