def equal(a, b, c):
    return len([x for x in list((a,b,c)) if list((a,b,c)).count(x) > 1])


print(equal(1,4,3))
