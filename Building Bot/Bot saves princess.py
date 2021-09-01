#!/usr/bin/python

def displayPathtoPrincess(n,grid):
	# find princess and mario
	for index, row in enumerate(grid):
		if 'p' in row:
			princess = (index, row.index('p'))
		if 'm' in row:
			mario = (index, row.index('m'))
	
	diffRows = princess[0] - mario[0]
	diffCols = princess[1] - mario[1]

	print(''.join([
		'UP\n' * abs(diffRows) if diffRows < 0 else 'DOWN\n' * diffRows,
		'LEFT\n' * abs(diffCols) if diffCols < 0 else 'RIGHT\n' * diffCols]))

m = int(input())
grid = [] 
for i in range(0, m): 
	grid.append(input().strip())

displayPathtoPrincess(m,grid)