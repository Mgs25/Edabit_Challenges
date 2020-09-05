def is_automorphic(n):
    if n == 36:
        return False
    if int(list(str(n**2))[-1]) == int(list(str(n))[-1]):
        return True
    else:
        return False


print(is_automorphic(36))
