cardNums = ['4123456789123456'
			,'42536258796157867'       	#17 digits in card number → Invalid 
			,'4424444424442444'        	#Consecutive digits are repeating 4 or more times → Invalid
			,'5122-2368-7954 - 3214'   	#Separators other than '-' are used → Invalid
			,'44244x4424442444'        	#Contains non digit characters → Invalid
			,'0525362587961578'			#Doesn't start with 4, 5 or 6 → Invalid
        ]
import re

nonDigitsPatern = r'[a-zA-Z]'

def procCardNum(cardNum):
	lst = [True if len(item) % 4 == 0 else False for item in cardNum.split('-')]

	return not lst.count(False)

def countConsDigit(cardNum):
	lst = set(list(cardNum))
	for item in lst:
		if cardNum.count(item) >= 4:
			return False
		else:
			continue
	return True


def isValid(cardNum):
	return 'Valid' if (len(''.join(cardNum.split('-'))) == 16) and procCardNum(cardNum) and (cardNum[0] in ['4', '5', '6']) and not (' ' in list(cardNum)) and countConsDigit(cardNum) and not (re.findall(cardNum, nonDigitsPatern)) else 'Invalid'

cardNum = cardNums[0]

# print(len(''.join(cardNum.split('-'))) == 16)

TESTER = re.compile(
	r"^"
	r"(?!.*(\d)(-?\1){3})"
	r"[456]"
	r"\d{3}"
	r"(?:-?\d{4}){3}"
	r"$")

print(TESTER.search(cardNum.strip()))
# for item in cardNums:
# 	# print(isValid(item))
# 	print(TESTER.search(item.strip()))