def square_digits(n):
    return "".join([str(int(num)**2) for num in str(n)])
print(square_digits(9119))
