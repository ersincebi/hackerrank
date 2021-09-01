# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def isPrime(param):
	flag = True
	if param == 2:
		flag = True
	elif param == 1 or param%2==0:
		flag = False
	else:
		for i in range(2, int(math.sqrt(param)+1)):
			if param % i == 0:
				flag = False
				break
	return 'Prime' if flag else 'Not prime'

# def isPrime(param):
# 	flag = True
# 	if param == 1:
# 		flag = False
# 	else:
# 		for i in range(2, int(math.sqrt(param)+1)):
# 			if param % i == 0:
# 				flag = False
# 				break
# 		flag = True
	# 	for i in range(2, int(math.sqrt(param))):
	# 		if param%i is 0:
	# 			flag = False
	# 			break

	# return 'Prime' if flag else 'Not prime'
lst = ['1',
'4',
'9',
'16',
'25',
'36',
'49',
'64',
'81',
'100',
'121',
'144',
'169',
'196',
'225',
'256',
'289',
'324',
'361',
'400',
'441',
'484',
'529',
'576',
'625',
'676',
'729',
'784',
'841',
'907']
# for num in lst:
#     print(isPrime(int(num)))
for _ in range(int(input())):
	print(isPrime(int(input())))
