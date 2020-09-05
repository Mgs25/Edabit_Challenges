binary_string = "01000010 01101001 01110000 01000010 01101111 01110000 01000010 01101001 01110000 01000010 01101111 01110000 00100000 01001001 00100000 01100001 01101101 00100000 01100001 00100000 01110010 01101111 01100010 01101111 01110100"

binary_code = binary_string.split()
decoded_array,result = [],[]
sep = ""
for code in binary_code:
    integer = int(code,2)
    decoded_array.append(integer)


for value in decoded_array:
    result.append(chr(value))
    
print(sep.join(result))
    
