a = [[0]*301 for _ in range(301)]
for i in range(1,301):
  x = i
  for j in range(1,301):
    if j == 1:
      a[i][j] = a[i-1][j] + i
    else:
      a[i][j] = a[i][j-1] + x
      x += 1
for t in range(int(input())):
  p,q = map(int,input().split())
  x,y = 0,0
  w,z = 0,0
  for i in range(1,301):
    for j in range(1,301):
      if a[i][j] == p:
        x = i
        y = j
      if a[i][j] == q:
        w = i
        z = j
  k = x+w
  c = y+z
  print(f'#{t+1} {a[k][c]}')