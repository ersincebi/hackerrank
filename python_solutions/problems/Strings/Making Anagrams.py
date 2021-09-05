def makeAnagram(a, b):
	return set(list(a)) - set(list(b))

if __name__ == '__main__':
	print(makeAnagram('showman', 'woman'))
