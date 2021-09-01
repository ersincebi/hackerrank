import math
import os
import random
import re
import sys

def checkMagazine(magazine, note):
	truthTable = [True if magazine.count(item) >= note.count(item) else False for item in set(sorted(note))]
	print(set(sorted(note)))
	print(truthTable)
	print('No' if False in truthTable else 'Yes')
	
if __name__ == '__main__':
	'''
	6 5
	two times three is not four
	two times two is four
	'''
	# first_multiple_input = input().rstrip().split()

	# m = int(first_multiple_input[0])

	# n = int(first_multiple_input[1])

	magazine = 'apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg'.rstrip().split()

	note = 'elo lxkvg bg mwz clm w'.rstrip().split()

	checkMagazine(magazine, note)
