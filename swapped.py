def flip_end_chars(txt):
	is_compatible = True
	is_pair = False
	first,last = '',''
	if str(type(txt)).find('str') == -1:
		is_compatible = False
	elif len(txt) < 2:
		is_compatible = False
	elif txt[0] == txt[-1]:
		is_pair = True

	if is_compatible and not is_pair:
		first=txt[-1]
		last=txt[0]
		return first+txt[1:-1]+last
	elif is_pair:
		return "Two's a pair."
	else:
		return "Incompatible."
print(flip_end_chars("a"))