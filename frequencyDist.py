def get_frequencies(lst):
	dict = {}
	for element in set(sorted(lst)):
		dict[element] = lst.count(element)
	return dict

print(get_frequencies(["A", "B", "A", "A", "A"]))
#output : { "A" : 4, "B" : 1 }