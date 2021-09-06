def insertionSort2(n, arr):
	# Write your code here
	for i in range(1, n):
		key = arr[i]
		
		j = i-1
		
		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
			
		arr[j + 1] = key
		print(*arr)

insertionSort2(6, [1, 4, 3, 5, 6, 2])