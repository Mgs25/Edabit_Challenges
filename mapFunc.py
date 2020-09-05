lst = [1,2,3,4,5,6]
def addBoi(a):
	return ("this is {}".format(a))

result = map(addBoi,lst)

print(list(result))