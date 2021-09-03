def bigSorting(unsorted):
	# Write your code here
	return [str(n) for n in sorted(unsorted, key = lambda x: int(x))]


print(bigSorting([
					'1',
					'3',
					'3',
					'5',
					'10',
					'31415926535897932384626433832795'
					]))