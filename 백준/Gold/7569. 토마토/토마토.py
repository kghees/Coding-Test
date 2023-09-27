from collections import deque
import sys
input = sys.stdin.readline
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
def bfs():
  while q:
    x,y,z = q.popleft()
    for k in range(6):
      nx = x + dx[k]
      ny = y + dy[k]
      nz = z + dz[k]
      if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
        if a[nx][ny][nz] == 0:
          a[nx][ny][nz] = a[x][y][z] + 1
          q.append((nx,ny,nz))
m,n,h = map(int,input().split())
a = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if a[i][j][k] == 1:
        q.append((i,j,k))
bfs()
result = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if a[i][j][k] > result:
        result = a[i][j][k]
for i in range(h):
  for j in range(n):
    for k in range(m):
      if a[i][j][k] == 0:
        result = -1
if result == -1:
  print(-1)
else:
  print(result-1)