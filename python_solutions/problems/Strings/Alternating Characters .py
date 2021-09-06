# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
	n = len(s)
	count = 0
	for i in range(n-1):
		if s[i] == s[i+1]:
			count+=1

	return count

if __name__ == '__main__':
	q = [
		'AAAA',
		'BBBBB',
		'ABABABAB',
		'BABABA',
		'AAABBB'
	]

	for q_itr in q:
		print(alternatingCharacters(q_itr))
