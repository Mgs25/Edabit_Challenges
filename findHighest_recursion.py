def find_highest(lst):
	return max(lst[0],find_highest(lst[:-1]))
def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))

print(maximum([-1, 3, 5, 6, 99, 12, 2]))