def ordered_matrix(a, b):
    matrix = []
    n = 1
    for i in range(a*b):
        matrix.append(i+1)
    return matrix
print(ordered_matrix(2,2))
