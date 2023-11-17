for t in range(10):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(100)]
  res = 0
  for i in range(100):
    x = sum(a[i])
    y = 0
    w,z = 0,0
    if res < x:
      res = x
    for j in range(100):
      y += a[j][i]
    if res < y:
      res = y
    w += a[i][i]
    z += a[i][99-i]
    if res < w:
      res = w
    if res < z:
      res = z
  print(f'#{t+1} {res}')