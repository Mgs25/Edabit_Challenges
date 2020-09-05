def minutes_to_seconds(time):
	t = time.split(":")
	if int(t[1]) > 60:
		return False
	else:
		return int(t[0])*60+int(t[1])

print(minutes_to_seconds("01:00"))