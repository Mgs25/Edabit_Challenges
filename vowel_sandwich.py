def is_vowel_sandwich(s):
    vowels = "aeiou"
    if len(s) > 3:
        return False
    if list(s)[0] not in vowels and list(s)[-1] not in vowels:
        if list(s)[1] in vowels:
            return True
    return False
print(is_vowel_sandwich("ear"))
