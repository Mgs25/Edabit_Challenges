def not_share(lst1, lst2):
	return True if len(set(lst2+lst1)) == len(lst1+lst2) else False
print(not_share([1, 2, 3], [4, 5, 6]))