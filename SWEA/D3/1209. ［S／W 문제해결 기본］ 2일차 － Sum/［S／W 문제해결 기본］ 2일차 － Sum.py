for t in range(10):
  n = int(input())
  arr = [list(map(int,input().split())) for _ in range(100)]
  x = 0
  for i in range(100):
    a = sum(arr[i])
    if a > x:
      x = a
  y = 0
  for i in range(100):
    b = 0
    for j in range(100):
      b += arr[j][i]
    if b > y:
      y = b
  z = 0
  c, d = 0, 0
  for i in range(100):
    c += arr[i][i]
    d += arr[i][99-i]
    if max(c,d) > z:
      z = max(c,d)
  w = max(x,y,z)
  print(f'#{t+1} {w}')