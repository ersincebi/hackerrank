#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def fltr(num):
	if num >= 2:
		return num
	
	return

def sherlockAndAnagrams(s):
	res = 0
	arr = {}
	for i in range(len(s)):
		for j in range(len(s) - i):
			s1 = ''.join(sorted(s[j:j + i + 1]))
			arr[s1] = arr.get(s1, 0) + 1

	for e in arr:
		res += int(arr[e]*(arr[e]-1)/2)
		
	
	return res

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# q = int(input().strip())

	for q_itr in ['abba', 'abcd']:
		# s = input()

		result = sherlockAndAnagrams(q_itr)
		
		print(result)
	#     fptr.write(str(result) + '\n')

	# fptr.close()
