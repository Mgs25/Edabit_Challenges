def how_many_missing(lst):
	return sum([1 for i in range(lst[0],lst[-1]) if i not in lst])

print(how_many_missing([1, 2, 3, 8, 9]))