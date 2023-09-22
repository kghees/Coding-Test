from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y):
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if d[nx][ny] == 0:
        continue
      if d[nx][ny] == 1:
        d[nx][ny] = d[x][y] + 1
        q.append((nx,ny))
  return d[n-1][m-1]
n,m = map(int,input().split())
d = [list(map(int,input())) for _ in range(n)]
print(bfs(0,0))