import numpy as np

toInt = lambda x: list(map(int, x.strip().split()))

n, m, p = toInt(input())

print(np.array([toInt(input()) for _ in range(m+n)]))