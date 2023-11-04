from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if (0 <= nx < n and 0 <= ny < m) and a[nx][ny] == 0:
        a[nx][ny] = a[x][y] + 1
        q.append((nx,ny))
m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
q = deque()
for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      q.append((i,j)) 
bfs()
res = max([max(i) for i in a])
for i in range(n):
  for j in range(m):
    if a[i][j] == 0:
      res = -1
      break
  if res == -1:
    break
if res == -1:
  print(-1)
else:
  print(res-1)