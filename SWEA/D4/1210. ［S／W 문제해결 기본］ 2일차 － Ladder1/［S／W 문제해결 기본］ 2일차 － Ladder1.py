dx = [1,0,0]
dy = [0,1,-1]
for _ in range(1,11):
  t = int(input())
  a = [list(map(int,input().split())) for _ in range(100)]
  res = 0
  for i in range(100):
    if a[0][i] == 1:
      x,y = 0,i
      d = 0
      while x < 99:
        if d == 0:
          if y > 0 and a[x][y-1] == 1:
            d = 2
          elif y < 99 and a[x][y+1] == 1:
            d = 1
        else:
          if a[x+1][y] == 1:
            d = 0
        x += dx[d]
        y += dy[d]
        if a[x][y] == 2:
          res = i
          break
  print(f'#{t} {res}')