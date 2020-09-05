def missing_num(lst):
    increment = (max(lst) - min(lst)) / len(lst)
    for i in lst:
        if i+increment not in lst:
            return i+increment
print(missing_num([1,2,4,5,6]))
