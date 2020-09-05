def flip(txt, spec):
    if spec == 'word': return ' '.join([x[::-1] for x in txt.split()])
    else: return ' '.join([x for x in txt.split()][::-1])
txt = "There's never enough time to do all the nothing you want"
print(flip(txt,"sentence"))