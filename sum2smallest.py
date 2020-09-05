def sum_two_smallest_nums(lst):
	sortedList = sorted([x for x in lst if x > 0])
	return sum(sortedList[0:2])

print(sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))