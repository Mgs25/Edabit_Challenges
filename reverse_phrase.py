string = "?driew tib a kool ti seoD"
solved = ["" for x in range(len(string))]
sep = ""
i = 0
j = 0
for i in range(len(string)):
    i+=1
    solved[j] = string[(len(string)-i)]
    j+=1
    
print(sep.join(solved))

    

