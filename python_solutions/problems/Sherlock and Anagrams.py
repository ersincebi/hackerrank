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
import numpy as np
def sherlockAndAnagrams(s):
	map = {}
	for i in range(len(s)):
		for j in range(len(s) - i):
			s1 = ''.join(sorted(s[j:j + i + 1]))
			map[s1] = map.get(s1, 0) + 1
	vals = np.unique((np.array(list(map.values())) >= 2),  return_counts=True)
	print(vals[1][1])

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# q = int(input().strip())

	# for q_itr in range(q):
	# s = input()

	# result = 
	# sherlockAndAnagrams('ifailuhkqq')
	sherlockAndAnagrams('kkkk')

	# fptr.write(str(result) + '\n')

	# fptr.close()
