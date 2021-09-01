import numpy

numpy.set_printoptions(legacy='1.13')

print(numpy.linalg.det([list(map(float, input().strip().split())) for _ in range(int(input()))]))