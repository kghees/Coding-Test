from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y):
  global z
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if a[x][y] + 1 == a[nx][ny]:
          z += 1
          q.append((nx,ny))
  return z
for t in range(int(input())):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(n)]
  cnt = 1
  index = 1e9
  for i in range(n):
    for j in range(n):
      z = 1
      z = bfs(i,j)
      if cnt < z:
        cnt = z
        index = a[i][j]
      elif cnt == z:
        if index > a[i][j]:
          index = a[i][j]
  print(f'#{t+1} {index} {cnt}')