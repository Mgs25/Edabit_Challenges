def find_bob(names):
	try:
		return names.index("Bob")
	except ValueError:
		return -1

print(find_bob(["Jimmy", "Layla"]))