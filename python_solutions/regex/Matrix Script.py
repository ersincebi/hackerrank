#!/bin/python3

import math
import os
import random
import re
import sys

matrix = [
					'Tsi'
					,'h%x'
					,'i #'
					,'sM '
					,'$a '
					,'#t%'
					,'ir!'
				]
n = len(matrix)
m = len(matrix[0])


res = ""

for zipped in zip(*matrix):
	# print(zipped)
	res += "".join(zipped)

# print(res)
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", res))