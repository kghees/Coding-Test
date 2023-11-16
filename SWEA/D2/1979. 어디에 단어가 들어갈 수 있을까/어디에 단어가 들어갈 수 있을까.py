for t in range(int(input())):
  n,k = map(int,input().split())
  a = [list(map(int,input().split())) for _ in range(n)]
  res = 0
  for i in range(n):
    x,y = 0,0
    for j in range(n):
      if a[i][j] == 1:
        x += 1
      elif a[i][j] == 0:
        if x == k:
          res += 1
        x = 0
      if a[j][i] == 1:
        y += 1
      elif a[j][i] == 0:
        if y == k:
          res += 1
        y = 0
    if x == k:
      res += 1
    if y == k:
      res += 1
  print(f'#{t+1} {res}')