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
      if (0 <= nx < n and 0 <= ny < n):
        if ans[x][y] + a[nx][ny] < ans[nx][ny]:
          ans[nx][ny] = ans[x][y] + a[nx][ny]
          q.append((nx,ny))
for t in range(int(input())):
  n = int(input())
  a = [list(map(int,input())) for _ in range(n)]
  ans = [[1e9]*n for _ in range(n)]
  ans[0][0] = a[0][0]
  bfs(0,0)
  print(f'#{t+1} {ans[n-1][n-1]}')