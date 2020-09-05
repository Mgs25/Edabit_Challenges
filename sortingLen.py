def number_len_sort(lst):
	lst = map(str,lst)
	return list(map(int,sorted(lst,key=len)))



print(number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]))