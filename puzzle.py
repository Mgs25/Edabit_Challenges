def puzzle_pieces(a1, a2):
	return len(list(set([(x+y) for x,y in zip(a1,a2)]))) == 1

print(puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]))