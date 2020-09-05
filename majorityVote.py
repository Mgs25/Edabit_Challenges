def majority_vote(lst):
    try:return list(set([x for x in lst if lst.count(x) > len(lst)/2]))[0]
    except:return None
print(majority_vote(["A", "B", "B", "A", "C", "C"]))