def duplicate_count(txt):
    return len(list(set([x for x in txt if txt.count(x)>1])))


print(duplicate_count("Aa"))