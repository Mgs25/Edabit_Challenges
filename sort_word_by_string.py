def sort_by_string(lst, txt):
    lst,txt = list(lst),list(txt)
    out = []
    for letter in txt:
        for word in lst:
            if word.startswith(letter):
                out.append(word)

    return out

print(sort_by_string(["poof", "floof", "loop"], "flatp"))
