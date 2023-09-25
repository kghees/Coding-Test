from collections import deque
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
def bfs(x,y):
  if x == c and y == d:
    return 0
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for k in range(8):
      nx = x + dx[k]
      ny = y + dy[k]
      if nx < 0 or nx >= l or ny < 0 or ny >= l:
        continue
      if n[nx][ny] == 1:
        continue
      if n[nx][ny] == 0:
        n[nx][ny] = n[x][y] + 1
        q.append((nx,ny))
  return n[c][d]
for _ in range(int(input())):
  l = int(input())
  n = [[0]*l for _ in range(l)]
  a,b = map(int,input().split())
  c,d = map(int,input().split())
  print(bfs(a,b))