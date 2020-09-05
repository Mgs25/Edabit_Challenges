def matrix(x, y, z):
	mainList = []

	for i in range(x):
		innerList = []
		for j in range(y):
			innerList.append(z)
		mainList.append(innerList)

	return mainList
	
print(matrix(2, 1, "edabit"))