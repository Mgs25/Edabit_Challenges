def is_smooth(sentence):
	sentence = sentence.split()
	return all([sentence[i][-1] == sentence[i+1][0] for i in range(len(sentence)-1)])
print(is_smooth("Marta appreciated deep perpendicular right trapezoids"))