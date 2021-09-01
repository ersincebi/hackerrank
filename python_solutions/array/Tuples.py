if __name__ == '__main__':
	n = 2 # int(input())
	integer_list = map(int, '1 2'.split())
	
	# 3713081631934410656
	print(hash(tuple(integer_list)))