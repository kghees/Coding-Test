for t in range(int(input())):
  h,w = map(int,input().split())
  a = []
  x,y = 0,0
  d = ''
  for i in range(h):
    s = list(input())
    a.append(s)
    for j in range(len(s)):
      if s[j] in ['^','v','>','<']:
        x,y = i,j
        d = s[j]
  n = int(input())
  m = list(input())
  for i in range(n):
    if m[i] == 'S':
      if d == '^':
        for j in range(x-1,-1,-1):
          if a[j][y] == '*':
            a[j][y] = '.'
            break
          elif a[j][y] == '#':
            break
      elif d == 'v':
        for j in range(x+1,h):
          if a[j][y] == '*':
            a[j][y] = '.'
            break
          elif a[j][y] == '#':
            break
      elif d == '<':
        for j in range(y-1,-1,-1):
          if a[x][j] == '*':
            a[x][j] = '.'
            break
          elif a[x][j] == '#':
            break
      elif d == '>':
        for j in range(y+1,w):
          if a[x][j] == '*':
            a[x][j] = '.'
            break
          elif a[x][j] == '#':
            break
    elif m[i] == 'U':
      d = '^'
      nx = x-1
      if nx < 0 or nx >= h:
        a[x][y] = d
        continue
      if a[nx][y] == '.':
        a[x][y] = '.'
        x = nx
      a[x][y] = d
    elif m[i] == 'D':
      d = 'v'
      nx = x+1
      if nx < 0 or nx >= h:
        a[x][y] = d
        continue
      if a[nx][y] == '.':
        a[x][y] = '.'
        x = nx
      a[x][y] = d
    elif m[i] == 'L':
      d = '<'
      ny = y-1
      if ny < 0 or ny >= w:
        a[x][y] = d
        continue
      if a[x][ny] == '.':
        a[x][y] = '.'
        y = ny
      a[x][y] = d
    elif m[i] == 'R':
      d = '>'
      ny = y+1
      if ny < 0 or ny >= w:
        a[x][y] = d
        continue
      if a[x][ny] == '.':
        a[x][y] = '.'
        y = ny
      a[x][y] = d
  print(f'#{t+1}',end=' ')
  for i in range(h):
    print(''.join(a[i]))