'''
All of the characters are the same, e.g. aaa.
	if 4 letter are same res = 1
	if 3 letter are same res = 2
	if 2 letter are same res = 3
	if 1 letter are same res = 4
	------------------------------
						total = 10

		res = counter * (counter + 1) / 2
				4	*	5	/	2 = 10

All characters except the middle one are the same, e.g. aadaa.
	aadaa

	lets say we take the char in the middle and investigate the neighbors
	the first evaluation also takes each string and adds to the result_counter
	for the second:
	example:	i:		letter:		neighbors:			comparison:		returns:	res_counter:
				1		a			i-1:a -> i+1:d		aad -> daa		false		0
				2		d			i-1:a -> i+1:a		ada -> ada		true		1
				3		a			i-1:d -> i+1:a		daa -> aad		false		1
				4		a			i-1:a -> i+1:a		aaa -> aaa		true		2
				-----------------------------------------------------------------------
																		in total = 4
																		but we should subtract 1 for the previous process
'''


def substrCount(n, s):
	counter = 0
	res = 0
	index = 0
	while index < n:
		counter = 1
		while index+1 < n and s[index] == s[index+1]:
			index += 1
			counter += 1

		res += counter * (counter + 1) / 2
		index += 1
	
	for index in range(1, n):
		counter = 1
		while (
			index + counter < n and
			s[index] != s[index - 1] and
			s[index - counter] == s[index + counter] and
			s[index - 1] == s[index - counter]
		):
			counter += 1

		res += counter - 1

	return res

print(substrCount(5, 'asasd'))		# expected 7
print(substrCount(4, 'aaaa'))		# expected 10
print(substrCount(7, 'abcbaba'))	# expected 10