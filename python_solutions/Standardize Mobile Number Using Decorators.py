def wrapper(f):
	def fun(l):
		f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
	return fun

@wrapper
def sort_phone(l):
	print(*sorted(l), sep='\n')

if __name__ == '__main__':
	l = [
		'07895462130',
		'919875641230',
		'9195969878',
	]
	# l = [input() for _ in range(int(input()))]
	sort_phone(l) 


