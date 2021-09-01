#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
	# Write your code here
	print('{0:.1f}'.format(sum([x*w for x,w in zip(X, W)]) / sum(W)))

if __name__ == '__main__':
	n = 5# int(input().strip())

	vals = list(map(int, '10 40 30 50 20 10 40 30 50 20'.rstrip().split()))

	weights = list(map(int, '1 2 3 4 5 6 7 8 9 10'.rstrip().split()))

	weightedMean(vals, weights)
