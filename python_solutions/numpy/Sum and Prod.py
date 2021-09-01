import numpy as np

toInt = lambda x: list(map(int, x.strip().split()))

arr = np.array([toInt(input()) for _ in range(toInt(input())[0])])

print(np.prod(np.sum(arr, axis=0)))