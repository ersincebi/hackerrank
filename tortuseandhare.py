nums = [1,2,4,1,3,5]

tortuse = nums[0]
hare = nums[0]

while True:
	tortuse = nums[tortuse]
	hare = nums[nums[hare]]
	if tortuse == hare:
		break

n1 = nums[0]
n2 = tortuse
while n1 != n2:
	n1 = nums[n1]
	n2 = nums[n2]

print(n1)