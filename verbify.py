def verbify(txt):
    txt = txt.split()
    if txt[0].endswith('e'):return f"{txt[0]}d {txt[1]}"
    elif txt[0].endswith('ed'):return f"{txt[0]}ed {txt[1]}"
    else:return f'{txt[0]} {txt[1]}'
print(verbify("shredded cheese"))