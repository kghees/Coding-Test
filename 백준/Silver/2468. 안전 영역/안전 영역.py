from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y,t):
  q = deque()
  q.append((x,y))
  check[x][y] = True
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if (0 <= nx < n and 0 <= ny < n) and not check[nx][ny]:
        if a[nx][ny] > t:
          check[nx][ny] = True
          q.append((nx,ny))
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = max([max(i) for i in a])
res = 1
for i in range(m):
  cnt = 0
  check = [[False]*n for _ in range(n)]
  for j in range(n):
    for k in range(n):
      if a[j][k] > i and not check[j][k]:
        bfs(j,k,i)
        cnt += 1
  res = max(res,cnt)
print(res)