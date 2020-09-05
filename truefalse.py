def check(num):
    return "yes"*(num%5==0) + " no"*(num%3==0)


print(check(15))
