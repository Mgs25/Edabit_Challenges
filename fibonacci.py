n = [1, 2, 4, 7]
lst = []

for i in range(0,len(n)-1,2):
	lst.append(sum(n[i:i+2]))
print(lst)