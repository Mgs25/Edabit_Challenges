import string

def is_palindrome(txt):
	A = string.ascii_lowercase
	finalTxt = ""
	for letter in txt.lower():
		if letter in A:
			finalTxt += letter
	return finalTxt == finalTxt[::-1]
	#return txt.lower() == txt[::-1].lower()

print(is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"))

#"AmanaplanacatahamayakayamahatacanalPanama"