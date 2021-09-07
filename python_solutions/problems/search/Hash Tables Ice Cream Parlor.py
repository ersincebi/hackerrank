def binarySearch(arr, start, stop, needle):
	if stop >= start:
		mid = (start + stop) // 2
		if arr[mid] == needle:
			return mid
		elif needle > arr[mid]:
			return binarySearch(arr, mid+1, stop, needle)
		else:
			return binarySearch(arr, start, mid-1, needle)
	else:
		return -1

def indexOf(arr, searchItem, exclude):
	for i in range(len(arr)):
		if arr[i] == searchItem and i != exclude:
			return i
		
	return -1

def get_indices(arr, val1, val2):
	i1 = indexOf(arr, val1, -1)
	i2 = indexOf(arr, val2, i1)

	return [min(i1, i2)+1, max(i1,i2)+1]

def whatFlavors(cost, money):
	n = len(cost)
	sortedCost = sorted(cost)

	for i in range(n):

		complement = money - sortedCost[i]
		loc = binarySearch(sortedCost, i+1, n-1, complement)

		if loc >= 0 and loc < n and sortedCost[loc] == complement:
			print(*get_indices(cost, sortedCost[i], complement))
			break

if __name__ == '__main__':
	
	whatFlavors(list(map(int, '1 4 5 3 2'.rstrip().split())), 4)	# expected 1 4
	whatFlavors(list(map(int, '2 2 4 3'.rstrip().split())), 4)		# expected 1 2
	whatFlavors(list(map(int, '7 2 5 4 11'.rstrip().split())), 12)	# expected 1 3