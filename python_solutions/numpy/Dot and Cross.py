import numpy as np

toInt = lambda x: list(map(int, x.strip().split()))

n = toInt(input())

A = np.array([toInt(input()) for _ in range(n[0])])
B = np.array([toInt(input()) for _ in range(n[0])])

print(np.dot(A, B))