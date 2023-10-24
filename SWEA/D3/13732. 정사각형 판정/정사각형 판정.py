def check(d,cnt,n):
  for i in range(n):
    for j in range(n):
      if d[i][j] == 1:
        down = 0
        right = 0
        for k in range(i+1,n):
          if d[k][j] == 1:
            down += 1
          else:
            break
        for l in range(j+1,n):
          if d[i][l] == 1:
            right += 1
          else:
            break
        if down != right:
          return False
        for x in range(i, i+down+1):
          for y in range(j, j+right+1):
            if d[x][y] == 1:
              cnt -= 1
            else:
              return False
        if cnt != 0:
          return False
        return True
for t in range(int(input())):
  n = int(input())
  a = [list(input()) for _ in range(n)]
  d = [[0]*n for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if a[i][j] == '#':
        d[i][j] = 1
        cnt += 1
  res = check(d,cnt,n)
  if res:
    print(f'#{t+1} yes')
  else:
    print(f'#{t+1} no')