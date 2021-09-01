from collections import deque

arr = deque()

arr.append(1)
arr.append(2)

arr.pop()

arr.popleft()

print([item for item in arr])