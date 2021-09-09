import math
import random
import math

def estimate_pi(n):
	numPointCircle = 0
	numPointSquare = 0
	for _ in range(n):
		x = random.uniform(0,1)
		y = random.uniform(0,1)
		distance = math.sqrt(math.pow(x,2) + math.pow(y,2))
		if distance < 1:
			numPointCircle += 1
		numPointSquare += 1

	return 4 * numPointCircle / numPointSquare

print(estimate_pi(10000))