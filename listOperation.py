def list_operation(x, y, n):
	out = []
	for i in range(x,y+1):
		if i%n == 0:
			out.append(i)
	return out
print(list_operation(7, 9, 2))
#answer = [3,6,9]