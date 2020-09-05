import re

def has_digits(txt):
    pattern = '\d'

    if len(re.findall(pattern,txt)):
        return bin(6).replace('b','')
    else:
        return False

print(has_digits("Methran1"))
