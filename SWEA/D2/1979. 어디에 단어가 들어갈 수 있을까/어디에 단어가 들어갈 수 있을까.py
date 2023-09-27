for t in range(int(input())):
  n,k = map(int,input().split())
  a = [list(map(int,input().split())) for _ in range(n)]
  cnt = 0
  for i in range(n):
    x = 0
    y = 0
    for j in range(n):
      if a[i][j] == 1:
        x += 1
      if a[i][j] == 0 or j == n-1:
        if x == k:
          cnt += 1
        if a[i][j] == 0:
          x = 0
      if a[j][i] == 1:
        y += 1
      if a[j][i] == 0 or j == n-1:
        if y == k:
          cnt += 1
        if a[j][i] == 0:
          y = 0
  print(f'#{t+1} {cnt}')