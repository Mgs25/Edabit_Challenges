import re

floatPattern = "[0-9]{1,}\.[0-9]"
intPattern = "\d{1,}"
def valid_str_number(n):
	if bool(re.match(floatPattern,n)):
		return "float"
	elif bool(re.match(intPattern,n)):
		return "int"
	else:
		return "Invalid"

print(valid_str_number("3..2"))