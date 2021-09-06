def countSort(arr):
	n = len(arr)
	count_arr = [0] * n
	output_arr = [0] * n

	for i in range(n):
		count_arr[int(arr[i][0])] += 1

	for i in range(1, len(count_arr)):
		count_arr[i] += count_arr[i-1]

	for i in range(n-1, -1, -1):
		output_arr[count_arr[int(arr[i][0])] - 1] = [arr[i][0], '-'] if i < n//2 else arr[i]
		count_arr[int(arr[i][0])] -= 1

	for i in range(n):
		arr[i] = output_arr[i][1]

	return arr

if __name__ == '__main__':
	n = 20

	arr = ['0 ab','6 cd','0 ef','6 gh','4 ij','0 ab','6 cd','0 ef','6 gh','0 ij','4 that','3 be','0 to','1 be','5 question','1 or','2 not','4 is','2 to','4 the']

	print(*countSort([item.rstrip().split() for item in arr]))
