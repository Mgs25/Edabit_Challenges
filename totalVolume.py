def total_volume(*boxes):
	volume = []
	for box in boxes:
		currentVol = box[0]*box[1]*box[2]
		volume.append(currentVol)
	return sum(volume)

	return sum([x for x in boxes])
print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))