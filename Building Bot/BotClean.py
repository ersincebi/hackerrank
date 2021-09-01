#!/usr/bin/python

import math
import sys

def die():
	sys.exit(0)

def display(board):
	for row in board:
		print(''.join(row))

def shortestDistance(bot, dirt):
	return math.sqrt(((dirt[0]-bot[0])**2) + ((dirt[1]-bot[1])**2))

def locateDirts(board):
	dirtLoc = []
	for index, row in enumerate(board):
		if 'd' in row:
			dirtLoc.append((row.index('d'), index))

	return dirtLoc

def update_position(posx, posy, dirties):
	nearest_dirt = []
	for i in range(len(dirties)):
		# Euclidean distance
		result = shortestDistance((posy, posx), dirties[i])
		nearest_dirt.append(result)

	# print(nearest_dirt, dirties)
	# print(sorted(zip(nearest_dirt,dirties)))
	# print(sorted(zip(nearest_dirt,dirties))[0][1])
	# die()

	return sorted(zip(nearest_dirt,dirties))[0][1] # [x for (y,x) in sorted(zip(nearest_dirt,dirties))]

# Head ends here

def next_move(posr, posc, board):
	if len(locateDirts(board)):
		next_dirt = update_position(posr, posc, locateDirts(board))
		directions = [
										# vertical moves
										[
											'UP',
											'DOWN'
										],
										# horizontal moves
										[
											'LEFT',
											'RIGHT'
										]
									]
		print(posr, posc)
		print(next_dirt)
		
		next_step = ((posc - next_dirt[0]), (posr - next_dirt[1]))

		print(next_step)

		print(directions[next_step[0]][next_step[1]])
	else:
		print('CLEAN')
	# if next_dirt[0] < posc:
	# 	print('UP')
	# elif next_dirt[0] > posc:
	# 	print('DOWN')
	# elif next_dirt[1] < posr:
	# 	print('LEFT')
	# elif next_dirt[1]  > posr:
	# 	print('RIGHT')
	# else:
	# 	print('CLEAN')

# Tail starts here

if __name__ == "__main__":
	pos = (1, 1) # [int(i) for i in input().strip().split()]
	board = [
						'-----',
						'-b---',
						'---d-',
						'---d-',
						'--d-d'
					]
	board = [list(row) for row in board]
	
	next_move(pos[0], pos[1], board)