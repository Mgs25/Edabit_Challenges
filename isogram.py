def cap_to_front(txt):
    phrase = []
    left = []
    
    for letter in txt:
        if letter.isupper():
            phrase.append(letter)
        else:
            left.append(letter)
    
    return "".join(phrase+left)

print(cap_to_front("APhpy"))