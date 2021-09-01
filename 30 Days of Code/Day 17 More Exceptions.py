#Write your code here
class Calculator:
	def __init__(self):
		pass
	def power(self, num, power):
		if num < 0 or power < 0:
			return 'n and p should be non-negative'
		return pow(num, power)
	
myCalculator=Calculator()
T=int(input())
for i in range(T):
	n,p = map(int, input().split())
	try:
		ans=myCalculator.power(n,p)
		print(ans)
	except Exception as e:
		print(e)