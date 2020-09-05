import math
def weight(r, h):
	PI = math.pi
	volume = (PI*(r**2)*h)*0.001
	
	return round(volume,2)
	
print(weight(30,60))