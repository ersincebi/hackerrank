from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
	if len(s) == 1:
		return 'YES'
	lst = list(s)
	freq = Counter(lst)
	findMostCommon = lambda x: Counter(x.values()).most_common(1)
	
	common = findMostCommon(freq)

	counter = 0
	for key, val in freq.items():
		tmp = abs(val - common[0][0])
		if tmp != 0:
			counter+=tmp

	return 'YES' if counter in [0,1] else 'NO'



if __name__ == '__main__':
	print(isValid('aaaabbcc'))				# expected NO
	print(isValid('aabbccddeefghi'))		# expected NO
	print(isValid('abcdefghhgfedecba'))		# expected YES
	print(isValid('aabbc'))					# expected YES
	print(isValid('aaaaabc'))				# expected NO
	print(isValid('xxxaabbccrry'))			# expected NO