def get_middle(word):
	middle = int(len(word)/2)
	if len(word)%2==0:
		return word[middle-1:middle+1]
	else:
		return word[middle]

print(get_middle("testing"))