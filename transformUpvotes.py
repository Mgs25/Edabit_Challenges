def transform_upvotes(txt):
	return [int(float(x[:-1])*1000) if 'k' in x else int(float(x)) for x in txt.split()]


print(transform_upvotes("5.5k 8.9k 32"))