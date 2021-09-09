class MedianFinder(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.nums = list()
		self.N = 0

	def addNum(self, num):
		"""
		:type num: int
		:rtype: None
		"""
		self.nums.append(num)
		self.N += 1
		sorted(self.nums)


	def findMedian(self):
		"""
		:rtype: float
		"""
		mid = self.N // 2
		if self.N % 2 == 1:
			median = self.nums[mid]
		else:
			n = self.N // 2
			median = (self.nums[(n)-1] + self.nums[n]) / 2
		
		print(median)

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.findMedian()
obj.addNum(3)
obj.addNum(4)
obj.findMedian()