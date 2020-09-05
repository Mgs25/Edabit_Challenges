def ascii_capitalize(txt):
    return "".join([x.upper() if ord(x)%2==0 else x.lower() for x in txt])
print(ascii_capitalize(("Oh what a beautiful morning.")))
