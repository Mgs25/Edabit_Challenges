def XO(txt):
    txt = txt.lower()
    if (txt.count("o") == txt.count("x")):
        return True
    else:
        return False

print(XO("xxoo"))