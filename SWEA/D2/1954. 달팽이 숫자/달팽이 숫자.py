dx = [0,1,0,-1]
dy = [1,0,-1,0]
def snail(num,x,y):
  if num > n*n:
    return
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == 0:
      d[nx][ny] = num
      snail(num+1,nx,ny)
  return
for t in range(int(input())):
  n = int(input())
  d = [[0]*n for _ in range(n)]
  d[0][0] = 1
  snail(2,0,0)
  print(f'#{t+1}')
  for i in range(n):
    for j in range(n):
      print(d[i][j], end=' ')
    print()