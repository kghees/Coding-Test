t = int(input())
res = []
for i in range(t):
  a,b,c,d = map(int,input().split())
  x = a/b
  y = c/d
  if x == y:
    res.append('DRAW')
  elif x > y:
    res.append('ALICE')
  else:
    res.append('BOB')
for k in range(t):
  print(f'#{k+1} {res[k]}')