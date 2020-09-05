def is_triplet(*args):
	t = sorted(args)
	
	if t[0]**2 + t[1]**2 == t[2]**2:
		return True
	else:
		return False


print(is_triplet(13, 5, 12))