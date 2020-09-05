def accum(txt):
	return '-'.join([str(txt[i]*(i+1)).capitalize() for i in range(len(txt))])
print(accum("abcd"))