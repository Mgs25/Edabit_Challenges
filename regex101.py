import re
"""
x = "[a-zA-Z]{5,}"


matches = list(re.findall(x,s))
"""
def reverse5(s):
	newString = s.split(' ')
	finalString = []
	for word in newString:
		if len(word) >= 5:
			finalString.append(word[::-1])
		else:
			finalString.append(word)
	return ' '.join(finalString)

print(reverse5("This is a typical sentence."))