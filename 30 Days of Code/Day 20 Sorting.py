#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
	n = 3 # int(input().strip())

	a = list(map(int, '3 2 1'.rstrip().split()))

	# Write your code here
	numberOfSwaps = 0
	for i in range(n):
		
		for j in range(n - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
				numberOfSwaps+=1

		
		if numberOfSwaps == 0:
			break

	print(f'Array is sorted in {numberOfSwaps} swaps.')
	print(f'First Element: {min(a)}')
	print(f'Last Element: {max(a)}')