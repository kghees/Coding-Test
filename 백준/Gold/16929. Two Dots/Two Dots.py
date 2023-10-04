dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(x,y,cnt,color):
  if check[x][y]:
    if cnt - d[x][y] >= 4:
      return True
    else:
      return False
  check[x][y] = True
  d[x][y] = cnt
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == color:
        if dfs(nx,ny,cnt+1,color):
          return True
  return False
n,m = map(int,input().split())
a = [input() for _ in range(n)]
d = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if check[i][j]:
      continue
    d = [[0]*m for _ in range(n)]
    ok = dfs(i,j,1,a[i][j])
    if ok:
      print('Yes')
      exit()
print('No')