def greet_people(names):
    return str(",".join(["Hello "+i for i in names ]))



print(greet_people(["Angela", "Joe"]))
