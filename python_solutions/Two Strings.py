#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
	return 'Yes' if set(s1) & set(s2) else 'No'

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# q = int(input().strip())

	# for q_itr in range(q):
		# s1 = input()

		# s2 = input()

	# result = 
	
	print(twoStrings('hello', 'world'))
	print(twoStrings('hi', 'world'))

	# fptr.write(result + '\n')

	# fptr.close()
