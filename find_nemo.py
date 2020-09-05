def find_nemo(sentence):
    print(sentence.find("Nemo"))


import re

def find_nemo(sentence):
    s = sentence.split()

    if "Nemo" in s:
        return "I found Nemo at {}!".format(s.index("Nemo")+1)
    else:
        return "I can't find Nemo :("

print(find_nemo("I am finding !"))