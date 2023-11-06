import sys
sys.setrecursionlimit(1000000)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(x,y):
  global cnt
  if not (0 <= x < n and 0 <= y < m):
    return False
  if a[x][y] == 1:
    a[x][y] = 0
    cnt += 1
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      dfs(nx,ny)
    return True
  return False
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
res = 0
cnt = 0
arr = []
for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      if dfs(i,j):
        res += 1
        arr.append(cnt)
        cnt = 0
x = 0
if arr:
  x = max(arr)
else:
  x = 0
print(res)
print(x)