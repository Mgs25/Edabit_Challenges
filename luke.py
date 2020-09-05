def relation_to_luke(name):
	relations = {
		"Darth Vader":"father",
		"Leia":"sister",
		"Han":"brother in law",
		"R2D2":"droid"
	}

	return "Luke, I am your {}".format(relations[name]+".")

print(relation_to_luke("Leia"))