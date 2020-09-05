def apocalyptic(n):
	if str(2**n).count('666')==0:return 'Safe'
	elif str(2**n).count('666')==1:return 'Single'
	elif str(2**n).count('666')==2:return 'Double'
	elif  str(2**n).count('666')==3:return 'Triple'
print(apocalyptic(931))