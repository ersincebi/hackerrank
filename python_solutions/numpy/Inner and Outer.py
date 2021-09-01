import numpy as np

toInt = lambda x: list(map(int, x.strip().split()))

A = np.array([toInt(input())])
B = np.array([toInt(input())])

print(np.inner(A, B)[0,0])
print(np.outer(A, B))