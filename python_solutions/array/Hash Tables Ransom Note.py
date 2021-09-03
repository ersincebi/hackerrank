import math
import os
import random
import re
import sys

from collections import Counter

def checkMagazine(magazine, note):
	# truthTable = [True if magazine.count(item) >= note.count(item) else False for item in set(sorted(note))]
	# print(set(sorted(note)), '\n', set(magazine))
	# res = list(dict(magazine).fromkeys(note))
	a = Counter(magazine)
	b = Counter(note)


	print("Yes" if ( a & b ) == b else "No")
	
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
