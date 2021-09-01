regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = [
		'110000'		# False
		,'111456'		# True
		,'abcdef'		# False
		,'101201'		# True
	]
for item in P:
	print(re.match(regex_integer_in_range, item))
	print(re.findall(regex_alternating_repetitive_digit_pair, item))
	print (bool(re.match(regex_integer_in_range, item)) 
	and len(re.findall(regex_alternating_repetitive_digit_pair, item)) < 2)