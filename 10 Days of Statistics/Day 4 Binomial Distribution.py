# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
	return 1 if n==0 else factorial(n-1) * n
	

def combination(n,x):
	return factorial(n) / (factorial(x) * factorial(n-x))

def binomial(x, n, p):
	return combination(n, x) * p**x * (1-p)**(n-x)


'''
The ratio of boys to girls for babies born in Russia is 1.09 : 1.
If there is 1 child born per birth, what proportion of Russian families with exactly 6
children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of
decimal places (i.e., format).
'''
arr = list(map(float, '1.09 1'.strip().split()))

odds = arr[0] / arr[1]

res = sum([binomial(i, 6, odds / (odds+1)) for i in range(3, 7)])
print('{0:.3f}'.format(res))

'''
A manufacturer of metal pistons finds that, on average 12%,
of the pistons they manufacture are rejected because they are incorrectly sized.
What is the probability that a batch of 10 pistons will contain:

1) No more than 2 rejects?
2) At least 2 rejects?
'''
arr = list(map(int, '12 10'.strip().split()))

res = sum([binomial(i, arr[0], arr[1]/100) for i in range(3)])
print('{0:.3f}'.format(res))


res = sum([binomial(i, arr[0], arr[1]/100) for i in range(2, arr[0]+1)])
print('{0:.3f}'.format(res))
