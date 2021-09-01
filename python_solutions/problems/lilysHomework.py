
def lilysHomework(arr):
	numOfSwaps = 0
	
	num1 = 0
	num2 = 0

	start = 0
	end = len(arr)-1

	temp = 0
	oldIndex = 0
	for _ in range(len(arr)):
		num1 = max(arr[start:end]) 
		num2 = min(arr[start:end])

		oldIndex = arr.index(num2)

		temp = arr[start]
		arr[start] = num2
		arr[oldIndex] = temp
		
		oldIndex = arr.index(num1)

		temp = arr[end]
		arr[end] = num1
		arr[oldIndex] = temp

		numOfSwaps += 1

		flag = 0
		i = 1
		while i < len(arr): 
				if(arr[i] < arr[i - 1]): 
						flag = 1
				i += 1
		
		if not flag:
			break

	return numOfSwaps


print(lilysHomework(list(map(int, '2 5 3 1'.rstrip().split()))))