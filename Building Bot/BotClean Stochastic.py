#!/bin/python3

import sys

global target

def display(board):
	for row in board:
		print(''.join(row))

def overrideBoard(posr, posc, board, val):
		board[abs(posc)][abs(posr)] = val

def nextMove(posr, posc, board):
	global target
	if abs(posc) < len(board[0])-1 and abs(posr) < len(board)-1:
		for row, col in enumerate(board):
			if 'd' in col:
				target = (row, col.index('d'))

		
		diffRows = posr - target[0]
		diffCols = posc - target[1]
		
		# print(target, diffRows, diffCols)
		# sys.exit(0)
		# 			(0, 4) 					0 			-4
		# b---d
		# -----
		# -----
		# -----
		# -----

		overrideBoard(posr, posc, board, '-')
		
		if diffCols < 0:
			print('RIGHT')
			posr += 1
		elif diffCols > 0:
			print('LEFT')
			posr -= 1
		elif diffRows < 0:
			print('DOWN')
			posc += 1
		elif diffRows > 0:
			print('UP')
			posc -= 1

		overrideBoard(posr, posc, board, 'b')
		# display(board)
		# print((posr, posc))

	return ""

if __name__ == "__main__":
	# pos = [int(i) for i in input().strip().split()]
	# board = [[j for j in input().strip()] for i in range(5)]
	pos = (0,0)
	board = [
		'b----',
		'-----',
		'-----',
		'-----',
		'd----'
	]
	display(board)
	print()


	board = [[colItem for colItem in row] for row in board]
	
	nextMove(pos[0], pos[1], board)