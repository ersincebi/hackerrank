#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
	total = 0
	for i in range(1, len(arr)):
		j = i-1
		key = arr[i]
		
		while (j >= 0) and (arr[j] > key):
			arr[j+1] = arr[j]
			j -= 1
			total += 1
			
		arr[j+1] = key

	return total


arr = list(map(int, '2 1 3 1 2 '.rstrip().split()))

print(runningTime(arr))
