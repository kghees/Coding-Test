n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
arr = sorted(a, key = lambda x: -x[2])
print(*arr[0][:2])
print(*arr[1][:2])
x = 2
if arr[0][0] == arr[1][0]:
  while arr[0][0] == arr[x][0]:
    x += 1
print(*arr[x][:2])