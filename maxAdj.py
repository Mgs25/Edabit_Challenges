def adjacent_product(lst):
	adjProd = []

	for i in range(len(lst)-1):
		adjProd.append(lst[i]*lst[i+1])

	return max(adjProd)

print(adjacent_product([5, 6, -4, 2, 3, 2, -23]))