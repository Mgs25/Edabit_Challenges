def century(year):
	n = -(-year//100)
	return '{} century'.format(str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th")))
print(century(1567))