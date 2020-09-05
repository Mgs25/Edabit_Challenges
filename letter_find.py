def letter_counter(lst, letter):
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if letter == lst[i][j]:
                count+=1
    return count

lst = [
    ['D', 'E', 'Y', 'H', 'A', 'D'],
    ['C', 'B', 'Z', 'Y', 'J', 'K'],
    ['D', 'B', 'C', 'A', 'M', 'N'],
    ['F', 'G', 'G', 'R', 'S', 'R'],
    ['V', 'X', 'H', 'A', 'S', 'S']
]

print(letter_counter(lst,'D'))