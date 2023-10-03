from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
m,n = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
d = [[-1]*m for _ in range(n)]
q = deque()
q1 = deque()
q.append((0,0))
d[0][0] = 0
while q:
  x,y = q.popleft()
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if d[nx][ny] == -1:
        if a[nx][ny] == 0:
          d[nx][ny] = d[x][y]
          q.append((nx,ny))
        else:
          d[nx][ny] = d[x][y] + 1
          q1.append((nx,ny))
  if not q:
    q = q1
    q1 = deque()
print(d[n-1][m-1])