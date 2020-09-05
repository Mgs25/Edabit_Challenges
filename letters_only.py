def letters_only(txt):
    final = []
    spc = ""
    for char in txt:
        if(char.isalpha()):
            final.append(char)
    return spc.join(final)

print(letters_only("R!=:~0o0./c&}9k`60=y"))