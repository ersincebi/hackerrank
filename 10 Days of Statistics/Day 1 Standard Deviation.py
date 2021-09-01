#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
import math

def stdDev(arr):
	# Print your answers to 1 decimal place within this function
	n = len(arr)
	u = sum(arr) / n

	print('{0:.1f}'.format(math.sqrt(sum([(num-u)**2 for num in arr]) / n)))

if __name__ == '__main__':
	n = 5 # int(input().strip())

	vals = list(map(int, '10 40 30 50 20'.rstrip().split()))

	stdDev(vals)
