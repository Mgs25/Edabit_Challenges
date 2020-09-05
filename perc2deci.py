import re
def dec_con(perc):
    return [float(re.sub("%","",perc[i]))/100 for i in range(len(perc))]

print(dec_con(["98.1%","13%","3%"]))
