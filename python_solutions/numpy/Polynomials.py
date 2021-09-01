import numpy as np

toInt = lambda x: list(map(float, x.strip().split()))

print(np.polyval(toInt(input()), toInt(input())[0]))