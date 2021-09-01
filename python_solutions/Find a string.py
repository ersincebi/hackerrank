def count_substring(string, sub_string):
	# if list(sub_string) not in list(string):
	# 	return 0
	count = 0
	for i in range(len(string)):
		if string[i:].startswith(sub_string):
			count += 1
	return count

if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()
	
	count = count_substring(string, sub_string)
	print(count)