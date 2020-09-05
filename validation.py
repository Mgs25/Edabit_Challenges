def is_valid_PIN(pin):
    if len(pin) == 4 or 6:
        for char in pin:
            if char.isalpha():
                return "INVALID ONLY NUMBERS"
    else:
        return "invalid"


print(is_valid_PIN("1aaa"))
