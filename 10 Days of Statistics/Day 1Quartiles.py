#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def median(arr):
	n = len(arr)
	mid = n // 2
	if n % 2 == 1:
		X = arr[mid]
	else:
		X = int((arr[(n//2)-1] + arr[n//2]) / 2)
	
	return X

def quartiles(arr):
	# Write your code here
	arr = sorted(arr)
	n = len(arr)
	mid = n // 2
		
	upperHalf = arr[-mid:]
	lowerHalf = arr[:mid]
	
	return median(lowerHalf), median(arr), median(upperHalf)
	
if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = 9# int(input().strip())

	data = list(map(int, '3 7 8 5 12 14 21 13 18'.rstrip().split()))
	'''
		6
    12
    16
	'''
	# data = list(map(int, '3 7 8 5 12 14 21 15 18 14'.rstrip().split()))
	'''
		7
		13
		15
	'''
	data = list(map(int, '4 17 7 14 18 12 3 16 10 4 4 12'.rstrip().split()))
	'''
		4
		11
		15
	'''

	res = quartiles(data)

	print('\n'.join(map(str, res)))
	# fptr.write('\n'.join(map(str, res)))
	# fptr.write('\n')

	# fptr.close()
