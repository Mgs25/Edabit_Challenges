def peel_layer_off(lst):
	peelOff = []
	
	for i in lst[1:-1]:
		peelOff.append(i[1:-1])

	return peelOff

print(peel_layer_off([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]]))