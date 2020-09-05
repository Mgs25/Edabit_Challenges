def replace_vowels(txt, ch):
    vowels = "aeiouAEIOU"
    out = []
    for letter in txt:
        if letter in vowels:
            out.append(ch)
        else:
            out.append(letter)
    return "".join(out)

print(replace_vowels("Hello Methran","#"))
