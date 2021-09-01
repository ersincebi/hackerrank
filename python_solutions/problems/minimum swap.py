def minimumSwaps(arr):
	swapCount = 0
	index = 0
	arr = [0] + arr
	sortedArr = sorted(arr)
	while arr != sortedArr:
		if index > len(arr):
			print(index)
		if arr[index] != index:
			arr[arr[index]], arr[index] = arr[index], arr[arr[index]]
			index = arr[index]
			swapCount += 1
		else:
			index += 1
	return swapCount

with open('./file') as file:

	arr = list(map(int, file.read().rstrip().split()))

	res = minimumSwaps(arr)

	print(res)