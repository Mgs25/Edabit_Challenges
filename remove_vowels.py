def remove_vowels(txt):
    return "".join([letter for letter in txt if letter not in "AEIOUaeiou"])


print(remove_vowels("METHRAN"))
