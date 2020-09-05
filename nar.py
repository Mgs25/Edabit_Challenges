def is_narcissistic(n):
	return sum([int(x)**len(str(n)) for x in str(n)]) == n


print(is_narcissistic(8208))