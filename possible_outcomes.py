def combinations(*args):
	res = 1
	for i in args:
		res *= i
	return res


print(combinations(3, 7, 4))