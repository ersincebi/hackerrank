import sys
def closestNumbers(arr):
	pairs = []
	arr = sorted(arr)
	n = len(arr)
	mn = sys.maxsize
	for i in range(n-1):
		tmp = arr[i+1] - arr[i]
		if tmp < mn:
			pairs = []
			pairs.append(arr[i])
			pairs.append(arr[i+1])
			mn = tmp
		elif tmp == mn:
			pairs.append(arr[i])
			pairs.append(arr[i+1])

	return pairs

print(
	closestNumbers(
		list(
			map(int, '-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470'.split(' '))
			)
		)
	)	# expected -520 -470 -20 30
print(
	closestNumbers(
		list(
			map(int, '-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854'.split(' '))
			)
		)
	)	# expected -20 30
print(
	closestNumbers(
		list(
			map(int, '5 4 3 2'.split(' '))
			)
		)
	)	# expected 2 3 3 4 4 5