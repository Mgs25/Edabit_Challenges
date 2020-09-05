from math import floor,ceil
def is_central(txt):
	mid = floor(len(txt)/2)
	txt = list(txt)
	for letter in txt:
		if letter != ' ':
			if txt.index(letter) == mid:
				return True
	return False

print(is_central("  l "))
