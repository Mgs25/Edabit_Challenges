def count_towers(towers):
	return towers[-1][0].count("##")

print(count_towers([
  ["     ##         "],
  ["##   ##        ##"],
  ["##   ##   ##   ##"],
  ["##   ##   ##   ##"]
]))