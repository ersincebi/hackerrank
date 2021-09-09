import numpy as np
m,n = [int(i) for i in '2 7'.strip().split(' ')]
data1=[
	'0.18 0.89 109.85',
	'1.0 0.26 155.72',
	'0.92 0.11 137.66',
	'0.07 0.37 76.17',
	'0.85 0.16 139.75',
	'0.99 0.41 162.6',
	'0.87 0.47 151.77'
]
X = []
Y = []
for item in data1:
	data = item.strip().split(' ')
	X.append(data[:m])
	Y.append(data[m:])
data2 = [
	'0.49 0.18',
	'0.57 0.83',
	'0.56 0.64',
	'0.76 0.18'
]

X_new = []
for item in data2:
	X_new.append(item.strip().split(' '))
X = np.array(X,float)
Y = np.array(Y,float)
X_new = np.array(X_new,float)

#center
X_R = X-np.mean(X,axis=0)
Y_R = Y-np.mean(Y)

#calculate beta
beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))

#predict
X_new_R = X_new-np.mean(X,axis=0)
Y_new_R = np.dot(X_new_R,beta)
Y_new = Y_new_R + np.mean(Y)

#print
for i in Y_new:
	print(round(float(i),2))