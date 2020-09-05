def construct_fence(p):
	cost = int(p.split("$")[1].replace(",",""))
	budget = 1000000

	return "H"*int(budget/cost)

print(construct_fence("$50,000"))
#("$1,000,000") ➞ "H"