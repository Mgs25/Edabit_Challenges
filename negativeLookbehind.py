import re

lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]
pattern = r'(?<!good )cookie'

regx = ', '.join(lst)

print(re.findall(pattern,regx))