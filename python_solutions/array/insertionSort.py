import time
n = 1000000000000000
start = time.microtime()
valid = [True if ((n ^ i) == (n + i)) else False for i in range(n)]
end = time.microtime()

print(valid)

print((end - start))