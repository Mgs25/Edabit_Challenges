def sum13(nums):
	RemovalIndex = []
	for i in range(len(nums)):
		if nums[i] == 13:
			RemovalIndex.append(i)
			if i+1 != len(nums):
				RemovalIndex.append(i+1)
	return RemovalIndex
#print(sum13([5, 13, 2]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))