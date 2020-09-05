def evenly_divisible(a, b, c):
    sum = 0
    for i in range(a,b):
        if i%c == 0:
            sum += i
    if sum == 0:
        return 0
    return sum

print(evenly_divisible(1,10,2))
