dx = [1,0,0]
dy = [0,1,-1]
for _ in range(10):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(100)]
  ans = 1e9
  res = 0
  for i in range(100):
    if a[0][i] == 1:
      x,y = 0,i
      cnt = 1
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
        cnt += 1
      if ans > cnt:
        ans = cnt
        res = i
  print(f'#{n} {res}')