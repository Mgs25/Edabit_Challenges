def special_reverse(s, c):
    result = ""
    for words in s.split():
        if words.startswith(c):
            result += " " + words[::-1]
        else:
            result += " " + words
    return result


print(special_reverse("word searches are super fun", "s"))
