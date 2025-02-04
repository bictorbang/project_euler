# Number Letter Counts

hash_map = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
            10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
            20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6,
            100: 7, 1000: 8}

# Refactorisation

def letters(n):
    if n % 1000 == 0:
        return letters(n // 1000) + hash_map[1000]
    if n % 100 == 0:
        return letters(n // 100) + hash_map[100]
    if n in hash_map: 
        return hash_map[n]
    if n > 100: 
        return letters(n // 100) + hash_map[100] + 3 + letters(n%100)
    return letters((n // 10) * 10) + letters(n % 10)

def number_letter_counts(n = 1_000):
    return sum(map(letters, range(1, n + 1)))

'''
# n < 1 001
def number_letter_counts2(n = 1_000):
    res = 0
    for i in range(1, n + 1):
        if i == 100: 
            res += hash_map[i] + 3
        elif i == 1000:
            res += hash_map[i] + 3
        elif i in hash_map:
            res += hash_map[i]
        elif i < 100:
            ten = (i // 10) * 10
            digit = i % 10
            res += hash_map[ten] + hash_map[digit]
        else:
            hund = i // 100
            if i % 100 == 0:
                res += hash_map[hund] + hash_map[100]
            elif i % 100 in hash_map:
                res += hash_map[hund] + hash_map[100] + 3 + hash_map[i%100]
            else:
                ten = ((i%100)// 10) * 10
                digit = i % 10
                res += hash_map[hund] + hash_map[100] + 3 + hash_map[ten] + hash_map[digit]
    return res
'''
    
def compute():
    return str(number_letter_counts())
    
if __name__ == "__main__":
    print(compute())

