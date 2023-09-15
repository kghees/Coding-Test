def dfs(x,y):
  if x <= -1 or x >= n or y <= - 1 or y >= n or visited[x][y] == 1:
    return
  if a[x][y] == -1:
    visited[x][y] = 1
    return
  visited[x][y] = 1
  dfs(x+a[x][y],y)
  dfs(x,y+a[x][y])
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dfs(0,0)
if visited[-1][-1] == 1:
  print('HaruHaru')
else:
  print('Hing')