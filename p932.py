# 2025

# Bruteforce...

def N_number(n = 4):
    i = 4
    total = 0
    while (s := i*i) < 10**n:
        if is_2025_number(s):
            total += s
        i += 1
    return total

def is_2025_number(number):
    m = len(str(number))
    for i in range(m):
        e = 10**(i+1)
        l = number // e
        r = number % e
        if (l + r)**2 == number and valid_concat(l, r, m):
            print(l, r)
            return True
    return False

def valid_concat(l, r, m):
    if l == 0 or r == 0: return False
    return len(str(l) + str(r)) == m
print(N_number(16))