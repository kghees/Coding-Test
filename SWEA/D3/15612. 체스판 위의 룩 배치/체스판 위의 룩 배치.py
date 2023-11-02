dx = [0,0,-1,1]
dy = [-1,1,0,0]
def chess(x,y):
  cnt = 0
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    while True:
      if not (0 <= nx < 8 and 0 <= ny < 8):
        break
      if a[nx][ny] == 'O':
        break
      if a[nx][ny] == '.':
        cnt += 1
      nx += dx[k]
      ny += dy[k]
  if cnt == 14:
    return True
  else:
    return False
for t in range(int(input())):
  a = [list(input()) for _ in range(8)]
  res = 0
  check = True
  for i in range(8):
    for j in range(8):
      if a[i][j] == 'O':
        res += 1
        if chess(i,j):
          continue
        else:
          check = False
          break
    if not check:
      break
  if check and res == 8:
    print(f'#{t+1} yes')
  else:
    print(f'#{t+1} no')