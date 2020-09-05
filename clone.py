def clone(lst):
	lst.append(list(lst))

	return lst


print(clone([1,2,3]))