def name_shuffle(txt):
    val = []
    final = []
    val.append(txt.split(" "))
    val[0][0],val[0][1] = val[0][1],val[0][0]
    for i in range(len(val)):
        for j in range(len(val[0])):
            final.append(val[i][j])
            
    return " ".join(final)





print(name_shuffle("Donald Trump"))