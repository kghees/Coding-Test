d = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
for tc in range(int(input())):
  n, m = map(int,input().split())
  arr = [[0]*n for _ in range(n)]
  mid = n // 2
  arr[mid][mid] = 2
  arr[mid-1][mid-1] = 2
  arr[mid][mid-1] = 1
  arr[mid-1][mid] = 1
  for _ in range(m):
    x,y,t = map(int,input().split())
    x, y = x - 1, y - 1
    data = []
    for i in range(8):
      dx,dy = d[i]
      nx = dx + x
      ny = dy + y
      while True:
        if not (0<=nx<n and 0<=ny<n):
          data = []
          break
        if arr[nx][ny] == 0:
          data = []
          break
        if arr[nx][ny] == t:
          break
        else:
          data.append((nx,ny))
        nx,ny = nx+dx,ny+dy
      for tx,ty in data:
        if t == 1:
          arr[tx][ty] = 1
        elif t == 2:
          arr[tx][ty] = 2
      arr[x][y] = t
    w, b = 0,0
    for i in range(n):
      w += arr[i].count(2)
      b += arr[i].count(1)
  print(f'#{tc+1} {b} {w}')    