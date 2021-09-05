avgA, avgB = [float(num) for num in '0.88 1.55'.split(" ")]

costA = 160 + 40*(avgA + avgA**2)
costB = 128 + 40*(avgB + avgB**2)

print(costA)
print(costB)