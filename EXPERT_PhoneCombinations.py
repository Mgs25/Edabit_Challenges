def letter_combinations(digits):
	NumMap = {
		'2':'abc',
		'3':'def',
		'4':'ghi',
		'5':'jkl',
		'6':'mno',
		'7':'pqrs',
		'8':'tuv',
		'9':'wxyz'
	}
	Combinations = []
	if len(digits) == 2:
		digit1 = digits[0]
		digit2 = digits[1]
		for i in NumMap[digit1]:
			for j in NumMap[digit2]:
				Combinations.append(i+j)
	else:
		digit1 = digits[0]
		digit2 = digits[1]
		digit3 = digits[2]
		for i in NumMap[digit1]:
			for j in NumMap[digit2]:
				for k in NumMap[digit3]:
					Combinations.append(i+j)	
	return Combinations
print(letter_combinations("23"))