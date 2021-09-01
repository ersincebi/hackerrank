#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
	# Write your code here
	maximum = 0
	for i in range(1,N+1):
		for j in range(1,i):
			tmp = i & j
			if maximum < tmp < K:
				maximum = tmp
			if maximum == K-1:
				return maximum
	return maximum
if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# t = int(input().strip())
	testArr = [
		'5 2',
		'8 5',
		'2 2'
	]
	for t_itr in testArr:
		first_multiple_input = t_itr.rstrip().split()

		count = int(first_multiple_input[0])

		lim = int(first_multiple_input[1])

		res = bitwiseAnd(count, lim)
		print(res)
# 	fptr.write(str(res) + '\n')

# fptr.close()
