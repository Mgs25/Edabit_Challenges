import re

pattern = "^/users/edabit/"

path = "/users/edabit/python/regex.py"
path1 = "/users/edabitt/python/file.jpg"

print(bool(re.match(pattern,path1)))