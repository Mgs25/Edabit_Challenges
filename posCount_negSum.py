def sum_neg(lst):
	pos = []
	neg = []
	for number in lst:
		if number > 0:
			pos.append(number)
		else:
			neg.append(number)
	if len(lst) != 0:
		return [len(pos),sum(neg)]
	else:
		return []
print(sum_neg([0,0]))