#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
	res = []
	mx = max(list(map(max, queries)))
	data = [0] * (int(mx)+1)
	for x, n in queries:
		if x == 1:
			data[n] += 1
		elif x == 2:
			if n in data and data[n] > 0:
				data[n] -= 1
		else:
			res.append(1 if n in set(data) else 0)
	return res

if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	# q = int(input().strip())

	queries = [
		'1 3',
		'2 3',
		'3 2',
		'1 4',
		'1 5',
		'1 5',
		'1 4',
		'3 2',
		'2 4',
		'3 2'
	]
	queriess = []
	for item in queries:
		queriess.append(list(map(int, item.split(' '))))

	ans = freqQuery(queriess)

	print(ans)
	# fptr.write('\n'.join(map(str, ans)))
	# fptr.write('\n')

	# fptr.close()
