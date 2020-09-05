def high_low(txt):
	lst = txt.split(' ')
	intLst = [int(x) for x in lst]
	return str(sorted(intLst)[-1])+' '+str(sorted(intLst)[0])
	#return sorted(lst)[0]+' '+sorted(lst)[-1]

print(high_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))