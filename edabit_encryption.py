def encrypt(word):
	algorithm = {"a":0,"e":1,"i":2,"o":2,"u":3}
	wordNew = list(word[::-1])
	encryptedString = ""

	for letter in wordNew:
		if letter in algorithm:
			encryptedString += str(algorithm[letter])
		else:
			encryptedString += letter

	return encryptedString+"aca"

print(encrypt("apple"))