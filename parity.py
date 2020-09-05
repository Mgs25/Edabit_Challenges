def parity_analysis(num):
	#odd -> num%2 == 0 (False)	
	#even -> num%2 == 0 (True)
	sum = 0
	for digit in str(num):
		sum += int(digit)
	
	return (sum%2==0) == (num%2==0)

print(parity_analysis(243))

"""
parity_analysis(243) ➞ True
# 243 is odd and so is 9 (2 + 4 + 3)
"""