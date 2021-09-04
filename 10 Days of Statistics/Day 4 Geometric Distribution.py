def geometrical(n, p):
	q = 1-p

	return q ** (n-1) * p

num, den  = list(map(int, '1 3'.split(' ')))
p = num / den
n = 5

print('{0:.3f}'.format(geometrical(n, p)))

res = sum([geometrical(x, p) for x in range(1, 6)])
print('{0:.3f}'.format(res))