dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]
for t in range(int(input())):
  n,m = map(int,input().split())
  d = [[0]*n for _ in range(n)]
  d[n//2-1][n//2-1] = 2
  d[n//2-1][n//2] = 1
  d[n//2][n//2-1] = 1
  d[n//2][n//2] = 2
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
        if d[nx][ny] == z:
          break
        if d[nx][ny] == 0:
          ans = []
          break
        else:
          ans.append((nx,ny))
        nx,ny = nx+dx[k], ny+dy[k]
      for i,j in ans:
        if z == 1:
          d[i][j] = 1
        elif z == 2:
          d[i][j] = 2
      d[x][y] = z
  w,b = 0,0
  for i in range(n):
    w += d[i].count(2)
    b += d[i].count(1)
  print(f'#{t+1} {b} {w}')