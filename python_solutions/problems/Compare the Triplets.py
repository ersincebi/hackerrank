#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
	# Write your code here
	a0, a1, a2 = a
	b0, b1, b2 = b
	resa = ( 1 if a0>b0 else 0 ) + ( 1 if a1>b1 else 0 ) + ( 1 if a2>b2 else 0 )
	resb = ( 1 if a0<b0 else 0 ) + ( 1 if a1<b1 else 0 ) + ( 1 if a2<b2 else 0 )
	
	return ' '.join([str(resa), str(resb)])

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	a = list(map(int, '17 28 30'.rstrip().split()))

	b = list(map(int, '99 16 8'.rstrip().split()))

	result = compareTriplets(a, b)

	print(result)
	# fptr.write(' '.join(map(str, result)))
	# fptr.write('\n')

	# fptr.close()
