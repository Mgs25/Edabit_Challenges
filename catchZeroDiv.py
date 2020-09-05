def catch_zero_division(expr):
	try:
		Evaluation = eval(expr)
		return False
	except:
		return True
print(catch_zero_division("2 / 0"))
