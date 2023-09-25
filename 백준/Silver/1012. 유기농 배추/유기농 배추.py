import sys
sys.setrecursionlimit(100000)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(x,y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  if a[x][y] == 1:
    a[x][y] = 0
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      dfs(nx,ny)
    return True
  return False
for t in range(int(input())):
  m,n,k = map(int,input().split())
  a = [[0]*m for _ in range(n)]
  for _ in range(k):
    u,v = map(int,input().split())
    a[v][u] = 1
  result = 0
  for i in range(n):
    for j in range(m):
      if a[i][j] == 1:
        if dfs(i,j):
          result += 1
  print(result)