import re

def flags(txt,pattern):
    return re.findall(pattern,txt)


regex = 'red flag|blue flag'
txt = "red flag blue flag"
print(flags(txt,regex))
