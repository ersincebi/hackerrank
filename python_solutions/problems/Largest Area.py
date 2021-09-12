import sys

def getMaxArea(w, h, isVertical, distance):
	# Write your code here
	maxAreas = []

	verticalLines = []
	verticalLines.append(0)
	verticalLines.append(w)
	horizontalLines = []
	horizontalLines.append(0)
	horizontalLines.append(h)

	n_vert = len(isVertical)

	maxHeight = h;
	maxWidth = w;

	for i in range(n_vert):
		if isVertical[i]:
			insert(verticalLines, distance[i])
			maxWidth = findMaxDistance(verticalLines)
		else:
			insert(horizontalLines, distance[i])
			maxHeight = findMaxDistance(horizontalLines)

		area = maxHeight * maxWidth
		maxAreas.append(area)

	return maxAreas

def findMaxDistance(lines):
	maxDistance = -sys.maxsize
	n = len(lines)-1
	while n > 0:
		maxDistance = max(maxDistance, lines[n] - lines[n-1])
		n-=1
	
	return maxDistance

def insert(lines, value):
	lines.append(value)
	n = len(lines)-1
	while (n > 0 and lines[n-1] > lines[n]):
		temp = lines[n-1]
		lines[n-1] = lines[n]
		lines[n] = temp
		n-=1
if __name__ == '__main__':
	w = 2

	h = 2

	isVertical = [0, 1]

	distance = [1, 1]

	result = getMaxArea(w, h, isVertical, distance)
	
	print(*result)

