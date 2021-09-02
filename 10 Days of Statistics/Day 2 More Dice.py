dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1) * len(dice2)
totalPossibilities = 0

for i in range(len(dice1)):
	for j in range(len(dice2)):
		if dice1[i] != dice1[j] and (dice1[i] + dice1[j]) == 6:
			totalPossibilities = totalPossibilities + 1

probability = totalPossibilities / total

print("Probability: {0}/{1} = {2}".format(totalPossibilities, total, probability))
