def card_hide(card):
    card = list(card)
    count = 0
    out = []

    for number in card:
        if count >= len(card) - 4:
            out.append(number)
        else:
            out.append("*")
        count += 1

    return "".join(out)
print(card_hide("1234123456785678"))
