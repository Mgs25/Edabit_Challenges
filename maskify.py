def maskify(txt):
	Mask = ""
	for i in range(len(txt[:-4])):
		Mask += "#"

	return Mask+txt[-4:]
print(maskify("64607935616"))