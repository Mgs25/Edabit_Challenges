def make_bricks(small, big, goal):
	sSize = small*1
	bSize = big*5
	sArray = [i for i in range(1,bSize+1) if i%5 == 0]
	bArray = [j for j in range(1,sSize+1)]
	
	if (goal not in sArray and goal not in bArray):
		for k in sArray:
			for l in bArray:
				if k+l == goal:
					return True
	else:
		return True

	return False

print(make_bricks(20, 4, 39))

#make_bricks(3, 2, 10) → True	