import re

digits = r'[0-9]'
upperAlphabets = r'[A-Z]'


def isEeryCountValid(uid):
    return 'Valid' if (len(uid) == 10) and (len(set(list(uid))) == len(list(uid))) and (len(re.findall(digits, uid)) >= 3) and (len(re.findall(upperAlphabets, uid)) >= 2) else 'Invalid'

inp = ['B1CD102354','B1CDEF2354']

for item in inp:
	print(isEeryCountValid(str(item)))

# print(checkAlpha(inp))