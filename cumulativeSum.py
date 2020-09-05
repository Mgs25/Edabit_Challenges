def cumulative_sum(lst):
	i = 0
	res = []
	for x in lst:
		res.append(x+sum(lst[0:i]))
		i += 1
	return res
	#return [x+sum(lst[0:lst.index(x)]) for x in lst]

print(cumulative_sum([3, 3, -2, 408, 3, 3, 0, 66, 2, -2, 2, 3, 4, 2, -47, 3, 3, 2]))

#[3, 6, 4, 412, 415, 418, 418, 484, 486, 484, 486, 489, 493, 495, 448, 451, 454, 456]