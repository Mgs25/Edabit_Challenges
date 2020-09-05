from math import sqrt

def get_distance(a, b):
	dist = sqrt((b["x"]-a["x"])**2+(b["y"]-a["y"])**2)
	return round(dist,3)
print(get_distance({"x": -2, "y": 1}, {"x": 4, "y": 3}))