def de_nest(lst):
	return str(str(lst).strip('['']'))


print(de_nest([[[[[[[[[[[[3]]]]]]]]]]]]))