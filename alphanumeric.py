import string

def alphanumeric_restriction(s):
    alphabets = string.ascii_lowercase
    numbers = string.digits
    type = ""

    if s[0] in numbers:
        type = "D"
    elif s[0] in alphabets:
        type = "A"

    if type == "A":
        for i in range(1,len(s)):
            if s[i] not in alphabets:
                return False
    if type == "D":
        for j in range(1,len(s)):
            if s[j] not in numbers():
                return False

    return True
print(alphanumeric_restriction("()"))
