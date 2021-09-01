#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

import statistics as st

def interQuartile(values, freqs):
	# Print your answer to 1 decimal place within this function
	arr = []
	for i in range(len(values)):
			arr += [values[i]] * freqs[i]

	arr = sorted(arr)

	N = sum(freq)

	if n%2 != 0:
			Q1 = st.median(arr[:N//2])
			Q3 = st.median(arr[N//2+1:])
	else:
			Q1 = st.median(arr[:N//2])
			Q3 = st.median(arr[N//2:])

	print('{0:.1f}'.format(float(Q3-Q1), 1))


if __name__ == '__main__':
	n = 6# int(input().strip())

	val = list(map(int, '6 12 8 10 20 16'.rstrip().split()))

	freq = list(map(int, '5 4 3 2 1 5'.rstrip().split()))

	interQuartile(val, freq)