def valid_str_number(n):
	try:
		if float(n):
			return True
		else:
			return True
	except:
		return False
print(valid_str_number("13"))