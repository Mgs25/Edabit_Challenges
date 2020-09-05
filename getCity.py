def grab_city(txt):
	return txt[txt.rfind('[')+1:-1]


print(grab_city("[Last Day!] Beer Festival [Munich]"))