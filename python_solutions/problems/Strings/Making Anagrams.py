def makeAnagram(a, b):
	countA = [0] * 26
	countB = [0] * 26

	index = 0
	while index<len(a):
		countA[ord(a[index]) - 97]+=1
		index+=1
	
	index = 0
	while index<len(b):
		countB[ord(b[index]) - 97]+=1
		index+=1

	res = 0
	for i in range(len(countA)):
		res += abs(countA[i] - countB[i])
	
	return res

if __name__ == '__main__':
	print(makeAnagram('showman', 'woman'))
