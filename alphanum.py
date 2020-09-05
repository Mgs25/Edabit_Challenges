def alphanumeric_restriction(s):
    if s.isnumeric():
        return True
    elif s.isalpha():
        return True
    else:
        return False


print(alphanumeric_restriction("18979836"))
