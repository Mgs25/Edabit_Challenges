def is_orthogonal(v1,v2):
    return False if sum(x*y for x, y in zip(v1, v2)) else True
print(is_orthogonal([3, -1], [7, 5]))