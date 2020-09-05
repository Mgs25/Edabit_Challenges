def space_weights(planet_a, weight, planet_b):
	weightIndex = {
		"Mercury":3.7,
		"Venus"  :8.87,
		"Earth"  :9.81,
		"Mars"   :3.711,
		"Jupiter":24.79,
		"Saturn" :10.44,
		"Uranus" :8.69,
		"Neptune":11.15
	}
	mass = (weight/weightIndex[planet_a])*weightIndex[planet_b]
	return round(mass,2)

print(space_weights("Earth", 1, "Mars"))
#0.38