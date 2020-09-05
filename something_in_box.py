def in_box(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if(lst[i][j] == "*"):
                return True
    return False

print(in_box([
  "#####",
  "#   #",
  "#####"
]))
