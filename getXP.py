def get_xp(d):
	xpPoints = 0
	xpSystem = {
		"Very Easy" : 5,
		"Easy" : 10,
		"Medium" : 20,
		"Hard" : 40,
		"Very Hard" : 80
	}

	for key in d:
		xpPoints += (d[key]*xpSystem[key])

	return str(xpPoints)+"XP"
print(get_xp({
  "Very Easy" : 85,
  "Easy" : 432,
  "Medium" : 157,
  "Hard" : 70,
  "Very Hard" : 90
}))
# ➞ "2055XP"

