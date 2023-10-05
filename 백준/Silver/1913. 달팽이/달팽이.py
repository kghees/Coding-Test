dx = [1,0,-1,0]
dy = [0,1,0,-1]
n = int(input())
t = int(input())
a = [[0]*n for _ in range(n)]
m = n**2
a[0][0] = m
x,y = 0,0
d = 0
m -= 1
while m > 0:
  nx = x + dx[d]
  ny = y + dy[d]
  if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 0:
    a[nx][ny] = m
    m -= 1
    x,y = nx,ny
  else:
    d = (d+1)%4
for i in range(n):
  for j in range(n):
    print(a[i][j],end=' ')
  print()
for i in range(n):
  for j in range(n):
    if a[i][j] == t:
      print(i+1,j+1)