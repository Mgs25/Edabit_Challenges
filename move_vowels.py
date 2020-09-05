import re

def is_vowel(letter):
    vowels = "aeiouAEIOU"
    if letter in vowels:
        return True
    else:
        return False
def split(txt):
    txt = list(txt)
    out = []
    for i in txt:
        if(is_vowel(i)):
            out.append(i)
            txt.remove(i)
    return "".join(out+txt) 
print(split("methran"))
