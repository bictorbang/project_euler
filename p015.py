# Lattice Paths

from functools import cache

@cache
def lattice_path(i = 20, j = 20):
    if (i, j) == (0, 0): return 1
    paths = lattice_path(i - 1, j) if i else 0
    paths += lattice_path(i, j - 1) if j else 0
    return paths

''' Using combinatorics
from math import comb

def lattice_path(n = 20):
    return comb(2*n, n)

Too long.
def lattice_path(n = 20, m = 20):
    res = []
    def lattice_dfs(n_1, m_1):
        if n_1 == n and m_1 == m:
            res.append(1)
            return
        if n_1 < n:
            lattice_dfs(n_1 + 1, m_1)
        if m_1 < m:
            lattice_dfs(n_1, m_1 + 1)

    lattice_dfs(0, 0)

    return sum(res)
'''

def compute():
    return str(lattice_path())
    
if __name__ == "__main__":
    print(compute())


