def is_strange_pair(txt1, txt2):
	if len(txt1) == 0 and len(txt2) == 0:
		return True
	elif len(txt1) == 0 and len(txt2) != 0:
		return False
	return (txt1[0] == txt2[-1]) and (txt1[-1]==txt2[0]) 

print(is_strange_pair("","abc"))