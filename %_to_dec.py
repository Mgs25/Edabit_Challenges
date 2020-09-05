import re
def dec_con(perc):
    return float(re.sub("%","",perc))/100

print(dec_con("98.1%"))
