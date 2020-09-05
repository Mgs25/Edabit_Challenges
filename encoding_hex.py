import codecs

string = "04 2f 22 33 38 31 35 28 2e 2f 1e 72 1e 32 2e 2d 34 35 28 2e 2f 1e 27 2d 20 26 1e 72 72 79 79 70 72 72 76"
bytes_array = []
final = []
sep = ""
string_arr = string.split()

for i in string_arr:
    bytes_array.append(codecs.decode(i,"hex"))

for j in range(len(bytes_array)):
    final.append(bytes_array[j].decode('utf-8'))

print(sep.join(final))