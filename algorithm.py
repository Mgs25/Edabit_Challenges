def encrypt(word):
	algorithm = {"a":0,"e":1,"i":2,"o":2,"u":3}
	return ''.join([str(algorithm[x]) if x in algorithm else x for x in word[::-1]])+'aca'
	