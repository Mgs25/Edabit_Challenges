def next_in_line(lst, num):
    if len(lst) != 0:
        for i in range(len(lst)-1):
            lst[i] = lst[i+1]
        lst[len(lst)-1] = num
    else:
        return "No list has been selected"
    
    return lst
def nextline(lst,num):
    return lst[1:] + [num] if lst else "no list has been selected"

print(nextline([],7))