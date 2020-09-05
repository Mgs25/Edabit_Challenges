def tuck_in(lst1,lst2):
	position = 1
	for number in lst2:
		lst1.insert(position,number)
		position += 1
	return lst1

#print(tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]))
print(tuck_in([[1, 2], [5, 6]], [[3, 4]]))