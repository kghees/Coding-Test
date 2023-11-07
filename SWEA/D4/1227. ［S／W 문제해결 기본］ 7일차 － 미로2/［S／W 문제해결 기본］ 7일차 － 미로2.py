from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y):
  q = deque()
  q.append((x,y))
  a[x][y] = 1
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < 100 and 0 <= ny < 100:
        if a[nx][ny] == 0:
          a[nx][ny] = 1
          q.append((nx,ny))
        elif a[nx][ny] == 3:
          a[nx][ny] = 1
          break
for t in range(1,11):
  n = int(input())
  a = [list(map(int,input())) for _ in range(100)]
  for i in range(100):
    for j in range(100):
      if a[i][j] == 2:
        bfs(i,j)
  res = 1
  for i in range(100):
    for j in range(100):
      if a[i][j] == 3:
        res = 0
  print(f'#{t} {res}')