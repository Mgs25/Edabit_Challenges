def is_special_array(lst):
	flag = True
	for i in range(0,len(lst),2):
		if lst[i]%2 != 0:
			flag = False
	for j in range(1,len(lst),2):
		if lst[j]%2 == 0:
			flag = False
	return flag

print(is_special_array([2, 7, 9, 1, 6, 1, 6, 3]))