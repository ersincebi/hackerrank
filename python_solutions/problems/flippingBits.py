def flippingBits(n):
	
	# [abs(int(i)-1) for i in "{:032b}".format(n)]
	return int(''.join([str(abs(int(i)-1)) for i in "{:032b}".format(n)]),2)

print(flippingBits(3))
