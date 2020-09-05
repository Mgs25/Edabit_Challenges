import string

def convert_binary(String):
	alphabets = list(string.ascii_lowercase)
	zeros = alphabets[alphabets.index("a"):alphabets.index("m")+1]
	bitCode = ""
	for letter in String.lower():
		if letter in zeros:
			bitCode += '0'
		else:
			bitCode += '1'
	return bitCode
print(convert_binary("house"))