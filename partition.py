def partition(txt, n):
	return [txt[i:i+n] for i in range(len(txt))]
print(partition("movement", 2))