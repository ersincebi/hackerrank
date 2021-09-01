def countTriplets(arr, r):
	'''
	loop i {

		index = arr.indexOf(formula(arr[i]))

		i = j

		****

		k

		formula
			a[n] = a * r [n-1]

	}


	'''
	index = 2

	print( arr[index] * (r ** (0 if index-1<0 else index-1)) )

	# i = 0
	# j = 1
	# k = 2
	counter = 0
	# ln = len(arr)
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			for k in range(j+1,len(arr)):
				series1 = [arr[i], arr[j], arr[k]]
				series2 = [arr[i], arr[j], arr[k] * r]
				
				print(series1, series2)
				# (r ** (0 if n-1<0 else n-1)
				
				

				# if arr[i] * (r ** (0 if i-1<0 else i-1)) == arr[j] or arr[j] * (r ** (0 if j-1<0 else j-1)) == arr[k]:
				# 	counter += 1
	# while True:
	# 	print(arr[i], arr[j+i], arr[k+i])

	

	# 	i += 1
	# 	if i + 3 > ln:
	# 		break
			
countTriplets(list(map(int, '1 2 2 4'.split(' '))), 2)