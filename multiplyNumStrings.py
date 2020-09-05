def multiply_nums(nums):
	return eval(nums.replace(', ','*'))
print(multiply_nums("2, 3, 4"))