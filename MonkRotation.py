t = int(input())
n,k = input().split()
arr = list(input().split(' '))

for i in range(int(k)):
    last = arr[-1]
    arr.insert(0,last)
    arr.pop()
print(arr)