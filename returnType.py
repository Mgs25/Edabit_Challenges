def get_type(value):
	return str(type(value)).split()[1].split('\'')[1]
	#return type(value).__name__

print(get_type(1))