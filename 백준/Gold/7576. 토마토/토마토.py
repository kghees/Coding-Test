from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
m,n = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
arr = [[-1]*m for _ in range(n)]
q = deque()
for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      arr[i][j] = 0
      q.append((i,j))
while q:
  x,y = q.popleft()
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < n and 0 <= ny < m:
      if a[nx][ny] == 0 and arr[nx][ny] == -1:
        arr[nx][ny] = arr[x][y] + 1
        q.append((nx,ny))
result = max([max(i) for i in arr])
for i in range(n):
  for j in range(m):
    if a[i][j] == 0 and arr[i][j] == -1:
      result = -1
print(result)