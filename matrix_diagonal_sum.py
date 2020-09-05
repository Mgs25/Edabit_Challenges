def trace(lst):
    count = 0
    out = []
    for i in range(len(lst)):
        print(lst[i][i])

print(trace([
  [1, 0, 1, 0],
  [0, 2, 0, 2],
  [3, 0, 3, 0],
  [0, 4, 0, 4]
]))
