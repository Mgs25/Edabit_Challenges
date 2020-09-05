def profit_margin(cost_price, sales_price):
	profit = (sales_price - cost_price) / sales_price
	return '{:.1%}'.format(profit)


print(profit_margin(75,40))
