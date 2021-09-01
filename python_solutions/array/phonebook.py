expList = [
	('Harry'
	,'37.21')
	,('Berry'
	,'37.21')
	,('Tina'
	,'37.2')
	,('Akriti'
	,'41')
	,('Harsh'
	,'39')
]
sortedList = sorted(expList,key=lambda x:x[1])
indexes = [index if sortedList[index][1] == sortedList[1][1] else 0 for index in range(len(sortedList))]

second_highest = sorted(list(set([marks for name, marks in expList])))[1]
print('\n'.join([a for a,b in sorted(expList) if b == second_highest]))
# indexes = sortedList[:1].index(sortedList[1])