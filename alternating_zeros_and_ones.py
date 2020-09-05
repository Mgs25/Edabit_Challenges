def can_alternate(s):
    return abs(str(s).count('0') - str(s).count('1')) in (0,1)


print(can_alternate(100100))
