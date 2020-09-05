from math import ceil
def DECIMATOR(txt):
	Key = ceil(5/10 * len(txt))
	return txt[:int(-Key)]

print(DECIMATOR(""))