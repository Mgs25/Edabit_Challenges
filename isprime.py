def is_prime(n):
	if n != 0 and n != 1:
		i = 2
		while i < n:
			if n % i == 0:
				return False
			i += 1
		return True
	else:
		return False
print(is_prime(4))