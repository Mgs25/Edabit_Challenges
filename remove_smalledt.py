def rem_small(lst):
    removed = False
    for number in lst:
        if number == min(lst):
            removed = True
            lst.remove(number)
    return lst

print(rem_small([5,2,1,4,6,1,3]))
