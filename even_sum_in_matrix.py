from math import floor,ceil
def sum_even(matrix):
    mid = 1.5
    print(mid,floor(mid),ceil(mid))
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] %2 == 0:
                sum += matrix[i][j]
    return sum


print(sum_even([
  [1, 0, 2],
  [5, 5, 7],
  [9, 4, 3]
]))
