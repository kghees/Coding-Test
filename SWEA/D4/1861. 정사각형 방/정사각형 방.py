from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(x,y):
  global cnt
  q = deque()
  q.append((x,y))
  while q:
    x,y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < n and 0 <= ny < n:
        if a[x][y] + 1 == a[nx][ny]:
          cnt += 1
          q.append((nx,ny))
  return cnt
for t in range(int(input())):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(n)]
  ans = [1e9,0]
  for i in range(n):
    for j in range(n):
      cnt = 1
      x = bfs(i,j)
      if x > ans[1]:
        ans[1] = x
        ans[0] = a[i][j]
      elif x == ans[1]:
        if ans[0] > a[i][j]:
          ans[0] = a[i][j]
  print(f'#{t+1}',*ans)