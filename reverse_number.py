def is_symmetrical(num):
    rev = reversed(str(num))
    
    if("".join(rev) == str(num)):
        return True
print(is_symmetrical(214412))