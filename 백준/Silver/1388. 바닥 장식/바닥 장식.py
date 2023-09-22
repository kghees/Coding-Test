n,m = map(int,input().split())
d = [input() for _ in range(n)]
cnt = 0
for i in range(n):
  a = ''
  for j in range(m):
    if d[i][j] == '-':
      if d[i][j] != a:
        cnt += 1
    a = d[i][j]
for j in range(m):
  a = ''
  for i in range(n):
    if d[i][j] == '|':
      if d[i][j] != a:
        cnt += 1
    a = d[i][j]
print(cnt)