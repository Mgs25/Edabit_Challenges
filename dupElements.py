def remove_dups(lst):
	newList = list(set(lst))
	return sorted(newList,key = lst.index)
print(remove_dups(['javascript', 'python', 'python', 'ruby', 'javascript', 'c', 'ruby']))

#['javascript', 'python', 'c', 'ruby'] should equal ['javascript', 'python', 'ruby', 'c']