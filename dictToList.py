def dict_to_list(d):
	return sorted([(key,d[key]) for key in d.keys()])

print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}))