import math

def factorial(n):
	return 1 if n == 0 else factorial(n-1) * n

def poison(l, k):
	return ((l ** k) * math.e ** (l * -1)) / factorial(k)

print(poison(0.88, 1.55))