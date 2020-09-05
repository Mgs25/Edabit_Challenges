import operator
def oldest(people):
	return max(people.items(), key=operator.itemgetter(1))[0]

print(oldest({
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}))