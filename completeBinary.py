def complete_binary(s):
	while len(s)%8 != 0:
		s = '0' + s
	return s
	

print(complete_binary("1101100"))