
count = 1
baseTwo = '{:b}'.format(439)
print(baseTwo)
if len(baseTwo)>1:
	for index in range(1, len(baseTwo)):
		if baseTwo[index-1] == baseTwo[index]:
			count+=1
		else:
			count=1
	
elif baseTwo==1 or baseTwo=='1':
	count = 1
else:
	count = 0
print(count)