def malthusian(food_growth, pop_mult):
	a,b,year = 100,100,0
	while b >= a:
		a *= pop_mult
		b += food_growth
		year += 1
	return year

print(malthusian(9433, 1.09))