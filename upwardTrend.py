def upward_trend(lst):
	for i in range(len(lst)-1):
		try:
			if lst[i] > lst[i+1]:
				return False
		except TypeError:
			return "Strings not permitted!"
	return True

print(upward_trend([1, 2, 3, 9]))