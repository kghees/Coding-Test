for t in range(1,11):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(100)]
  res = 0
  for i in range(100):
    x = sum(a[i])
    if x > res:
      res = x
  for i in range(100):
    w = 0
    for j in range(100):
      w += a[j][i]
    if w > res:
      res = w
  y,z = 0,0
  for i in range(100):
    y += a[i][i]
    z += a[i][99-i]
  k = max(y,z)
  if k > res:
    res = k
  print(f'#{t} {res}')