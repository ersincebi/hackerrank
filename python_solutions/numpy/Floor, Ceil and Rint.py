import numpy as np

np.set_printoptions(sign=" ")

arr = np.array(list(map(float, input().strip().split())))

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))