class Difference:
	def __init__(self, a):
		self.__elements = a

# Add your code here
	def computeDifference(self):
		index = 0
		arr = sorted(self.__elements)
		n = len(self.__elements) - 1
		diff = 0
		temp = 0
		while index < n//2:
			diff = arr[(n - index)] - arr[index]
			if diff > temp:
				temp = diff
			index += 1

		self.maximumDifference = temp  
            
# End of Difference class

# _ = input()
a = [1, 2, 5]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)