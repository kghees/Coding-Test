result = []
for t in range(int(input())):
  a,b,c,d = map(int,input().split())
  if a/b > c/d:
    result.append('ALICE')
  elif a/b < c/d:
    result.append('BOB')
  else:
    result.append('DRAW')
for k in range(t+1):
  print(f'#{k+1} {result[k]}')