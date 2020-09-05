def is_in_order(txt):
    return True if list(txt) == sorted(list(txt)) else False



print(is_in_order("abdc"))
