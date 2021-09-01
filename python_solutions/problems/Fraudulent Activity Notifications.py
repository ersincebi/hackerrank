#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
	total = 0
	for i in range(d, len(expenditure)):
		days = expenditure[i-d:i]
		arr = sorted(days)
		if d%2 != 0:
			median = arr[(d+1)//2 - 1]
		else:
			median = (arr[(d)//2 - 1] + arr[(d+1)//2])/2
		if expenditure[i] >= 2*median:
			total +=1
	return total

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# first_multiple_input = input().rstrip().split()

	# n = int(first_multiple_input[0])

	# d = int(first_multiple_input[1])

	# expenditure = list(map(int, input().rstrip().split()))

	# result = 
	print(activityNotifications(list(map(int, '1 2 3 4 4'.split())), 4))

	# fptr.write(str(result) + '\n')

	# fptr.close()
