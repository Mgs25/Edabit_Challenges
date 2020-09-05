def seq_level(*lst):
	out = [lst[x] - lst[x-1] for x in range(1,len(lst))]
	if (set(out) == 1):
		return "Linear"
	out = [lst[x] - lst[x-1] for x in range(1,len(lst))]
	if (set(out) == 1):
		return "Quadratic"
	lst = [lst[x] - lst[x-1] for x in range(1,len(lst))]
	if ((set(out)) == 1):
		return "Cubic"

print(seq_level(1,2,3,4,5))
