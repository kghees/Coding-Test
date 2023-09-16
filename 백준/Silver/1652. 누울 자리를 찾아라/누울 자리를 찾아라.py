n = int(input())
a = [list(input()) for _ in range(n)]
x,y = 0,0
for i in range(n):
  t1,t2 = 0, 0
  for j in range(n):
    if a[i][j] == '.':
      t1 += 1
    else:
      t1 = 0
    if t1 == 2:
      x += 1
    if a[j][i] == '.':
      t2 += 1
    else:
      t2 = 0
    if t2 == 2:
      y += 1
print(x, y)