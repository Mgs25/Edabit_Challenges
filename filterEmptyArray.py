def remove_empty_arrays(arr):
	return [x for x in arr if str(x) != '[]']
print(remove_empty_arrays([1, 2, [], 4]))