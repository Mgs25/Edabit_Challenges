def longest_nonrepeating_substring(txt):
	long,s,start = txt[0],txt[0],0
	for i in range(1, len(txt)):
		if txt[i] not in s:
			s+=txt[i]
			if len(s)>len(long):
				long=s
		else:
			start=txt.index(txt[i])+1
			txt = txt.replace(txt[i], '#', 1)
			s = txt[start:i+1]
	return long
print(longest_nonrepeating_substring("kjlmjsdeee"))
#									  0123456789
'''
for i in range(len(txt)-1):
		if (txt[i:i+2]) != txt[i]*2:
			print(txt[i:i+2])
'''