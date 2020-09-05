def unique(abb,word):
    count = 0
    for i in range(len(abb)):
        for j in abb:
            if word[i].startswith(j):
                print("word",word[i],"-",j)
                count+=1

    return True if count==len(word) else False

abb = ["b", "c", "ch"]
word =["broth", "chap", "cardigan"]
print(unique(abb,word))