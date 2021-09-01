#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
	# N = int(input().strip())
	testArr = [
		'riya riya@gmail.com',
		'julia julia@julia.me',
		'julia sjulia@gmail.com',
		'julia julia@gmail.com',
		'samantha samantha@gmail.com',
		'tanya tanya@gmail.com'
	]
	arr = []
	for N_itr in testArr:
		first_multiple_input = N_itr.rstrip().split()

		firstName = first_multiple_input[0]

		emailID = first_multiple_input[1]
		if '@gmail.com' in emailID:
			arr.append(firstName)
	
	arr = sorted(arr)
	for item in arr:
			print(item)