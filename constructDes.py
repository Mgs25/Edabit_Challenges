def construct_deconstruct(s):
	i = 0
	res = []
	while i<len(s):
		res.append(s[:i+1])
		i+=1
	i = i-1
	while i > 0:
		res.append(s[:i])
		i -= 1
	return res

print(construct_deconstruct("Hello"))