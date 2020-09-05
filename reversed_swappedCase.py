def reverse(txt):
    return "".join(list((reversed(txt.swapcase()))))


print(reverse("Hello World"))
