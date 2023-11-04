from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y):
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if not (0 <= nx < n and 0 <= ny < m):
        continue
      if a[nx][ny] == 0:
        continue
      if a[nx][ny] == 1:
        a[nx][ny] = a[x][y] + 1
        q.append((nx,ny))
n,m = map(int,input().split())
a = [list(map(int,input())) for _ in range(n)]
bfs(0,0)
print(a[n-1][m-1])