dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,-1,1]
for t in range(int(input())):
  n,m = map(int,input().split())
  a = [[0]*n for _ in range(n)]
  a[n//2-1][n//2-1] = 2
  a[n//2-1][n//2] = 1
  a[n//2][n//2-1]=1
  a[n//2][n//2] = 2
  for _ in range(m):
    x,y,z = map(int,input().split())
    x,y = x-1,y-1
    ans = []
    for k in range(8):
      nx = x + dx[k]
      ny = y + dy[k]
      while True:
        if not (0 <= nx < n and 0 <= ny < n):
          ans = []
          break
        if a[nx][ny] == 0:
          ans = []
          break
        if a[nx][ny] == z:
          break
        else:
          ans.append((nx,ny))
        nx += dx[k]
        ny += dy[k]
      for i,j in ans:
        if z == 1:
          a[i][j] = 1
        elif z == 2:
          a[i][j] = 2
      a[x][y] = z
  b,w = 0,0
  for i in range(len(a[i])):
    b += a[i].count(1)
    w += a[i].count(2)
  print(f'#{t+1} {b} {w}')