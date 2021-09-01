import sys

def display(board):
	for row in board:
		print(''.join(row))

import math

# Update cost that bot need to arrive the dirty
def update_position(posx, posy, dirties):
	nearest_dirt = []
	for i in range(len(dirties)):
		# Euclidean distance
		result = math.sqrt(((dirties[i][0] - posx) ** 2) + ((dirties[i][1] - posy) ** 2))
		nearest_dirt.append(result)
	return [x for (y,x) in sorted(zip(nearest_dirt,dirties))]

# Set the bot in your new position
def next_move(posx, posy, dimx, dimy, board):
	dirties = []
	for i in range(dimx):
		for j in range(dimy):
			if board[i][j] == 'd':
				dirties.append([i, j])

	next_dirt = update_position(posx, posy, dirties)
	if next_dirt[0][0] < posx:
		print('UP')
	elif next_dirt[0][0] > posx:
		print('DOWN')
	elif next_dirt[0][1] < posy:
		print('LEFT')
	elif next_dirt[0][1]  > posy:
		print('RIGHT')
	else:
		print('CLEAN')

if __name__ == "__main__":
	pos		= (0, 0)# [int(i) for i in input().strip().split()]
	dim		= (5, 5) # [int(i) for i in input().strip().split()]
	board = [
						'b---d',
						'-d--d',
						'--dd-',
						'--d--',
						'----d'
					]
	board = [board[i].split() for i in range(dim[0])]

	next_move(pos[0], pos[1], dim[0], dim[1], board)