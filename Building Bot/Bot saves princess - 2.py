def nextMove(n,r,c,grid):
	for index, row in enumerate(grid):
		if 'p' in row:
				princess = (index, row.index('p'))
		if 'm' in row:
				mario = (index, row.index('m'))

	diffRows = princess[0] - mario[0]
	diffCols = princess[1] - mario[1]

	if diffRows < 0: return 'UP'
	if diffRows > 0: return 'DOWN' 
	if diffCols < 0: return 'LEFT'
	else: return 'RIGHT'

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
	grid.append(input())

print(nextMove(n,r,c,grid))