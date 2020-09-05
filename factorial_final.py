def fact(num):
    fact = 1
    for number in range(0,num-1):
        fact *= (num - number)
    return fact
print(fact(5))
