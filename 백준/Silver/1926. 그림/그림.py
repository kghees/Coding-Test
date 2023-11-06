from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y):
  q = deque()
  q.append((x,y))
  cnt = 1
  a[x][y] = 0
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if (0 <= nx < n and 0 <= ny < m) and a[nx][ny] == 1:
        a[nx][ny] = 0
        cnt += 1
        q.append((nx,ny))
  return cnt
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
res = 0
arr = []
for i in range(n):
  for j in range(m):
    if a[i][j] == 1:
      res += 1
      arr.append(bfs(i,j))
x = 0
if arr:
  x = max(arr)
else:
  x = 0
print(res)
print(x)