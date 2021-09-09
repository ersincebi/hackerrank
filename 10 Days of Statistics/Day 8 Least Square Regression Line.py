n = 5
vals = [
	'95 85',
	'85 95',
	'80 70',
	'70 65',
	'60 70',
]
xy = [map(int, item.split()) for item in vals]
sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
a = (sy / n) - b * (sx / n)
print('{:.3f}'.format(a + b * 80))