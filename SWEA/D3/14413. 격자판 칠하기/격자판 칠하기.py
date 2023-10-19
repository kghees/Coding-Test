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
      if 0 <= nx < n and 0 <= ny < m:
        if a[nx][ny] == '?':
          if a[i][j] == '#':
            a[nx][ny] = '.'
          elif a[i][j] == '.':
            a[nx][ny] = '#'
        elif a[nx][ny] == a[i][j]:
          return False
  return True
for t in range(int(input())):
  n, m = map(int,input().split())
  a = [list(input()) for _ in range(n)]
  result = 1
  for i in range(n):
    for j in range(m):
      if bfs(i,j):
        continue
      else:
        result = 0
        break
    if result == 0:
      break
  if result == 1:
    print(f'#{t+1} possible')
  else:
    print(f'#{t+1} impossible')