for _ in range(10):
  t = int(input())
  a = [list(map(int,input().split())) for _ in range(100)]
  x = 99
  y = a[99].index(2)
  while x != 0:
    if 0 <= y < 99 and a[x][y+1] == 1:
      while y < 99 and a[x][y+1] == 1:
        y += 1
      x -= 1
    elif 0 < y < 100 and a[x][y-1] == 1:
      while y > 0 and a[x][y-1] == 1:
        y -= 1
      x -= 1
    else:
      x -= 1
  print(f'#{t} {y}')