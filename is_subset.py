def is_subset(subset,array):
    for i in subset:
        if i not in array:
            return False
    return True
subset,array = [1,2,3,7],[1,2,3,4,5]
print(is_subset(subset,array))
