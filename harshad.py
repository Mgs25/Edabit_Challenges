def is_harshad(num):
    return True if num % sum([int(x) for x in str(num)]) == 0 else False

print(is_harshad(666))
