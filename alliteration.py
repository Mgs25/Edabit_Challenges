def alliteration_correct(sentence):
	sentence = sentence.split()
	return [x.startswith(sentence[0][0]) or x.startswith(sentence[0][0].lower()) for x in sentence if len(x)>3]

print(alliteration_correct('She swam to the shore.'))