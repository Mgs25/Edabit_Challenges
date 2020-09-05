def count_palindromes(num1, num2):
    return sum([1 for x in range(num1,num2) if str(x) == str(x)[::-1]])

print(count_palindromes(878, 898))
