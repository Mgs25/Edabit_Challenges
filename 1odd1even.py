def one_odd_one_even(n):
	if int(str(n)[0])%2==0 and int(str(n)[1])%2!=0:
		return True
	elif int(str(n)[1])%2==0 and int(str(n)[0])%2!=0:
		return True 
	else:
		return False
print(one_odd_one_even(17)) #true