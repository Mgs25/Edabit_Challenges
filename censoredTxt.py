string1 = "*PP*RC*S*"
string2 = "UEAE"
j = 0
newString = ''

for i in range(len(string1)):
	if string1[i] == '*':
		newString +=	string2[j]
		j+=1
	else:
		newString += string1[i]

print(newString)