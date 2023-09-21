from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(d,a,b):
  n = len(d)
  q = deque()
  q.append((a,b))
  d[a][b] = 0
  count = 1
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if d[nx][ny] == 1:
        d[nx][ny] = 0
        q.append((nx,ny))
        count += 1
  return count
n = int(input())
d = [list(map(int,input())) for _ in range(n)]
cnt = []
for i in range(n):
  for j in range(n):
    if d[i][j] == 1:
      cnt.append(bfs(d,i,j))
cnt.sort()
print(len(cnt))
for i in cnt:
  print(i)