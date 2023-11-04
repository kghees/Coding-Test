dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
  global cnt
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  if a[x][y] == 1:
    cnt += 1
    a[x][y] = 0
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      dfs(nx,ny)
    return True
  return False
n = int(input())
a = [list(map(int,input())) for _ in range(n)]
cnt = 0
result = 0
arr = []
for i in range(n):
  for j in range(n):
    if a[i][j] == 1:
      if dfs(i,j):
        arr.append(cnt)
        result += 1
        cnt = 0
arr.sort()
print(result)
for i in arr:
  print(i)