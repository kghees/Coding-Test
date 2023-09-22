h,w = map(int,input().split())
c = [input() for _ in range(h)]
d = [[0]*(w) for _ in range(h)]
for i in range(h):
  cnt = 1
  cloud = False
  for j in range(w):
    if not cloud and c[i][j] == '.':
      d[i][j] = -1
    elif c[i][j] == 'c':
      cloud = True
      d[i][j] = 0
      cnt = 1
    elif cloud and c[i][j] == '.':
      d[i][j] = cnt
      cnt += 1
for i in d:
  print(*i,end=' ')
  print()