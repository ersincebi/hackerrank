import math


def normal_dist(x , mean , sd):
	return (math.pi*sd) * math.exp(-0.5*((x-mean)/sd)**2)

mean=20.0
sd=2.0

h1=19.5
h21,h22=20.0,22.0

phi = lambda x : (1 + math.erf(x))/2

print('{0:.3f}'.format(normal_dist(h1,mean,sd)))
print('{0:.3f}'.format(normal_dist((phi(h22) - phi(h21)),mean,sd)))

