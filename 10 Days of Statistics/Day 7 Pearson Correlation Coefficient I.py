N = 10
X = list(map(float,'10 9.8 8 7.8 7.7 7 6 5 4 2'.strip().split()))
Y = list(map(float,'200 44 32 24 22 17 15 12 8 4'.strip().split()))

u_x = sum(X) / N
u_y = sum(Y) / N

stdv_x = (sum([(i - u_x)**2 for i in X]) / N)**0.5
stdv_y = (sum([(i - u_y)**2 for i in Y]) / N)**0.5


covariance = sum([(X[i] - u_x) * (Y[i] - u_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))