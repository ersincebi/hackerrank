from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
	a = Counter(arr)
	b = Counter()
	s = 0
	for i in arr:
		j = i//r
		k = i*r
		a[i]-=1
		if b[j] and a[k] and not i%r:
			s+=b[j]*a[k]
		b[i]+=1
	return s

print(countTriplets(list(map(int, '1 2 2 4'.split(' '))), 2))