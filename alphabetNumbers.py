import string

def alph_num(txt):
	alphabets = string.ascii_lowercase
	index = {}
	out = ""

	for i in range(len(alphabets)):
		index[alphabets[i]] = i+1
	for letter in txt.lower():
		out += str(index[letter])+" "
	return out
print(alph_num("abz"))