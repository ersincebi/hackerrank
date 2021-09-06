import math

X = lambda n,u: n * u
O = lambda n,o: math.sqrt(n) * o

def centralLimit(X, U, O):
	return (0.5*(1 + math.erf(((X - U)/O)/(math.sqrt(2)))))

print('{0:.4f}'.format(centralLimit(9800, X(49, 205), O(49, 15))))

print('{0:.4f}'.format(centralLimit(500, X(100, 2.4), O(100, 2))))

marginOfError = 1.96 * 80/math.sqrt(100);

print('{0:.2f}\n{1:.2f}'.format((500 - marginOfError), (500 + marginOfError)))