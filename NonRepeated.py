def first_non_repeated_character(txt):
	try:
		return [x for x in txt if txt.count(x) == 1][0]
	except:
		return False


print(first_non_repeated_character("hheelloo"))