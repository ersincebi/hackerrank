import numpy as np

toInt = lambda x: list(map(int, x.strip().split()))

n = toInt(input())

arr = np.array([toInt(input()) for _ in range(n[0])])

print (arr.T)
print (arr.flatten())
