def sum67(nums):
	flag = False
	sum = 0
	for i in range(len(nums)):
		if nums[i] == 6:
			flag = True
		elif flag == True and nums[i] == 7:
			flag = False
		elif flag == False:
			sum += nums[i]
	return sum
print(sum67([2, 7, 6, 2, 6, 2, 7]))