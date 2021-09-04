def partition(arr):
	pivot = arr[0]
	left = []
	right = []
	for element in arr:
		if element<pivot:
			left.append(element)
		else:
			right.append(element)
	return left+right


arr = list(map(int, '4 5 3 7 2'.rstrip().split()))

print(*partition(arr))