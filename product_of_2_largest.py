def prod(lst):
    lst = (sorted(set(lst)))
    return (lst[-1]*lst[-2])
lst = [2,6,8,-2,4,4,1,0,-1,-1]

print(prod(lst))