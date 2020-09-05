def add_index(lst):
    for number in range(len(lst)):
        lst[number] = lst[number] + number
    return lst
    
print(add_index([0,0,0,0,0]))