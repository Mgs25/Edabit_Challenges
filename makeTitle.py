def make_title(txt):
	return ' '.join([x[0].upper()+x[1:] for x in txt.split()])

print(make_title("capitalize every word"))