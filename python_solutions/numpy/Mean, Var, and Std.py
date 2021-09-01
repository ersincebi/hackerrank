import numpy as np

toInt = lambda x: list(map(int, x.strip().split()))

arr = np.array([toInt(input()) for _ in range(toInt(input())[0])])

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))

print(np.round(np.std(arr), 11))

# 0.82915619759
# 0.82915619758885