
def insertionSort1(n, arr):
	# Write your code here
	# Traverse through 1 to len(arr)

	key = arr[-1]
	
	j = n-2
	
	# Move elements of arr[0..i-1], that are
	# greater than key, to one position ahead
	# of their current position
	while j >= 0 and key < arr[j]:
		arr[j + 1] = arr[j]
		print(*arr)
		j -= 1
		
	arr[j + 1] = key
	print(*arr)

insertionSort1(5, [2, 4, 6, 8, 3])