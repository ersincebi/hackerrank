import numpy as np

toInt = lambda x: map(int, x.strip().split()) 

n, m = toInt(input())

arrA = np.array([list(toInt(input())) for _ in range(n)])
arrB = np.array([list(toInt(input())) for _ in range(n)])

print(arrA + arrB)
print(arrA - arrB)
print(arrA * arrB)
print(arrA // arrB)
print(arrA % arrB)
print(arrA ** arrB)
