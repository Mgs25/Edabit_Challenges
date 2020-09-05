def remove_enemies(names, enemies):
    return [x for x in names if x not in enemies]



print(remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]))
