# Longest Collatz Sequence

from functools import cache

# Credits to Mikhail Lomonosov
def longest_collatz_sequence(n = 1_000_000):
    return max(range(1, n), key = collatz_sequence)
   
@cache
def collatz_sequence(n):
    if n == 1: return 1
    collatz_n = 3*n + 1 if n & 1 else n >> 1
    return collatz_sequence(collatz_n) + 1

'''
# Slow (around 23s)
def longest_collatz_sequence(n = 1_000_000):
    longest = 1
    longest_idx = 1
    for i in range(2, n+1):
        seq = [i]
        cur = i
        while seq[-1] != 1:
            if cur % 2 == 0:
                cur = cur // 2
                seq.append(cur)
            else:
                cur = 3*cur + 1
                seq.append(cur)
        if len(seq) > longest:
            longest_idx = i
            longest = len(seq)
        #longest = max(longest, len(seq))
        
    return longest_idx, longest
'''

def compute():
    return str(longest_collatz_sequence())
    
if __name__ == "__main__":
    print(compute())
