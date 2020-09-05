def steps_to_convert(txt):
    lower,upper = 0,0
    for letter in txt:
        if letter.isupper():
            upper += 1
        else:
            lower += 1
    return min(lower,upper)
print(steps_to_convert("abCDDDDDDDDDDDDsaodpasd"))
