'''
there are two strings at same lenght
s1 = ABCD
s2 = ABDC

lets say we delete C
	1. ABD
		we delete the 3th char
	2. ABD
		we delete the 4th char

or we delete D
	1. ABC
		we delete the 4th char
	2. ABC
		we delete the 3th char

in both outcomes we get the same result and same length from two strings,
in both example order stayed the same so there is no rearanging the strings
so we need to count than compare the combinations

formula for lengths in wiki:

			0	1	2	3	4	5	6	7
			Ø	M	Z	J	A	W	X	U
	0	Ø	0	0	0	0	0	0	0	0
	1	X	0	0	0	0	0	0	1	1
	2	M	0	1	1	1	1	1	1	1
	3	J	0	1	1	2	2	2	2	2
	4	Y	0	1	1	2	2	2	2	2
	5	A	0	1	1	2	3	3	3	3
	6	U	0	1	1	2	3	3	3	4
	7	Z	0	1	2	2	3	3	3	4

	if i or j == 0			then	result				= 0
	if i,j > 0 and c1==c2	then	lenght[i][j]		= lenght[i-1][j-1] + 1
	if i,j > 0 and c1!=c2	then	lenght[i][j]		= max(length[i][j-1], length[i-1][j])

'''

def commonChild(s1, s2):
	n = len(s1)
	m = len(s2)

	lengths = [[0] * (m + 1) for _ in range(n + 1)]

	for i, c1 in enumerate(s1):
		for j, c2 in enumerate(s2):
			if c1 == c2:
				lengths[i][j] = lengths[i - 1][j - 1] + 1
			else:
				lengths[i][j] = max(lengths[i][j - 1], lengths[i - 1][j])

	return lengths[n - 1][m - 1]

	
	return lengths[-1][-1]

print(commonChild('HARRY', 'SALLY'))		# expected 2
print(commonChild('AA', 'BB'))				# expected 0
print(commonChild('SHINCHAN', 'NOHARAAA'))	# expected 3
print(commonChild('ABCDEF', 'FBDAMN'))		# expected 2
print(commonChild('ABDC', 'ABCD'))			# expected 3
