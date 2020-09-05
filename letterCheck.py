def letter_check(lst):
	for letter in lst[1].lower():
		if lst[0].lower().find(letter.lower()) == -1:
			return False
	return True

print(letter_check(["THE EYES", "they see"]))