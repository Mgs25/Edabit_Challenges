def partially_hide(phrase):
    return ' '.join([x[0]+''.join(['-' for x in x[1:-1]])+x[-1] for x in phrase.split()])

print(partially_hide("She rolled her eyes"))