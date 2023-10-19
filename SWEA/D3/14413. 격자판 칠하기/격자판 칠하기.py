for t in range(int(input())):
  n,m = map(int,input().split())
  a = [list(input()) for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if a[i][j] == '#':
        if (i+j) % 2 == 0:
          x = '#'
          y = '.'
        else:
          x = '.'
          y = '#'
        break
      elif a[i][j] == '.':
        if (i+j) % 2 == 0:
          x = '.'
          y = '#'
        else:
          x = '#'
          y = '.'
        break
  result = 1
  for i in range(n):
    for j in range(m):
      if (i+j) % 2 == 0:
        if a[i][j] == y:
          result = 0
          break
      else:
        if a[i][j] == x:
          result = 0
          break
    if result == 0:
      break
  if result == 1:
    print(f'#{t+1} possible')
  else:
    print(f'#{t+1} impossible')