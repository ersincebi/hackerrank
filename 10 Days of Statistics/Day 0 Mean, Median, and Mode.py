# Enter your code here. Read input from STDIN. Print output to STDOUT

def mode(arr):
	distictArr = list(set(arr))
	dct = [(num, arr.count(num)) for num in distictArr]
	return sorted(dct, key=lambda x: (-x[1], x[0]))[0][0]

file_object = open('list')

data = file_object.read()

arr = list(map(int, '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'.strip().split()))

arr = sorted(arr)

arr = list(map(int, data.strip().split()))

n = len(arr) # input().strip().split()

print(float(sum(arr)/n))


print(float((arr[(n//2)-1]+arr[n//2])/2))

print(mode(arr))