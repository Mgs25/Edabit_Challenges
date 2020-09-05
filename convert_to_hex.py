import codecs
def convert_to_hex(txt):
    return ' '.join([codecs.encode(bytes(letter,'utf-8'),'hex').decode('utf-8') for letter in txt])
print(convert_to_hex("Big Boi"))