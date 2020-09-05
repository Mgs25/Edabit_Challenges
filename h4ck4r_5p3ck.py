def hacker_speak(txt):
	codeIndex = {'a': 4,'e': 3,'i': 1,'o': 0,'s': 5}
	res = ""

	for letter in txt:
		if letter in codeIndex:
			res += str(codeIndex[letter])
		else:
			res += letter

	return res

print(hacker_speak("javascript is cool"))