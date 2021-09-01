#!/bin/python3

import math
import os
import random
import re
import sys

global countL
global countR
#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def countInversions(arr):
	n = len(arr)
	if n==1:
		return 0
	R = n//2
	L = n - R
	halfR = arr[:R]
	halfL = arr[R:]
	res = countInversions(halfR) + countInversions(halfL)
	inversionR = 0
	inversionL = 0
	for i in range(n):
		if inversionR <R and (inversionL>=L or halfR[inversionR]<=halfL[inversionL]):
			arr[i] = halfR[inversionR]
			res += inversionL
			inversionR += 1 
		elif inversionL < L:
			arr[i] = halfL[inversionL]
			inversionL += 1
	return res

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# t = int(input().strip())

	# for t_itr in range(t):
	#     n = int(input().strip())

	arr = list(map(int, '2 1 3 1 2'.rstrip().split()))

	result = countInversions(arr)

	print(result)

	# fptr.write(str(result) + '\n')

	# fptr.close()
