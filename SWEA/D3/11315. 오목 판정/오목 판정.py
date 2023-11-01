dx = [0,1,1,1]
dy = [1,0,-1,1]
def omok(x,y):
  cnt = 1
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    while 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 'o':
      cnt += 1
      nx += dx[k]
      ny += dy[k]
    if cnt >= 5:
      return True
    else:
      cnt = 1
  return False
for t in range(int(input())):
  n = int(input())
  a = [list(input()) for _ in range(n)]
  check = False
  for i in range(n):
    for j in range(n):
      if a[i][j] == 'o':
        if omok(i,j):
          check = True
          break
        else:
          continue
    if check:
      break
  if check:
    print(f'#{t+1} YES')
  else:
    print(f'#{t+1} NO')