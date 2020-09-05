def double(word):
    for i in range(1,len(word)):
        if (word[i-1] == word[i]):
            return True
    return False
print(double("methrann is back"))
