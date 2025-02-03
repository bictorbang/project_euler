# Largest Palindrome Product

def is_palindrome(n):
    word = str(n)
    return word == word[::-1]

'''def largest_palindrome_product(n = 4):
    upper = 10**n
    lower = upper//2
    res = 0
    for i in range(lower, upper):
        for j in range(lower, upper):
            if is_palindrome(prod := i*j):
                res = max(res, prod)
    return res'''

def largest_palindrome_product(n = 3):
    return str(max(i*j for i in range(10**n // 2, 10**n) 
                       for j in range(10**n // 2, 10**n)
                       if is_palindrome(i*j)))


def compute():
    return str(largest_palindrome_product())
    
if __name__ == "__main__":
    print(compute())

