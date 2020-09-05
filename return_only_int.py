def return_only_integer(lst):
    lst = [x for x in lst if isinstance(x,int)]
    
    return lst

print(return_only_integer([1,"methran",True,4]))