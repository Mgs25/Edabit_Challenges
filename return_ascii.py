def counterpartCharCode(char):
    if(isinstance(char,int)):
        if(char.isupper()):
            return chr(char.lower())
    else:
        return ord(char)
    
    
    
print(counterpartCharCode("A"))