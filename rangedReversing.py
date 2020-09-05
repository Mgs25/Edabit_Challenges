def ranged_reversal(lst, start, finish):
    return lst[:start]+lst[start:finish+1][::-1]+lst[finish+1:]


print(ranged_reversal([1, 2, 3, 4, 5, 6], 1, 3))