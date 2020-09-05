def marathon_distance(d):
	sum = 0
	for dist in d:
		sum += abs(dist)
	if sum >= 25:
		return True
	else:
		return False
print(marathon_distance([-6, 15, 4]))