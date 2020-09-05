def tallest_skyscraper(lst):
	return [len(lst) - lst.index(i) for i in lst if i.count(1) >= 1][0]
print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]))