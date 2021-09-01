# Enter your code here. Read input from STDIN. Print output to STDOUT

day1, month1, year1 = [int(x) for x in '1 1 2010'.split(' ')]
day2, month2, year2 = [int(x) for x in '31 12 2009'.split(' ')]

if (year1, month1, day1) <= (year2, month2, day2):
	print(0)
elif (year1, month1) == (year2, month2):
	print(15 * (day1 - day2))
elif year1 == year2:
	print(500 * (month1 - month2))
else:
	print(10000)