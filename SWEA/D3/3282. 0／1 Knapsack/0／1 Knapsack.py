for t in range(int(input())):
  n, k = map(int,input().split())
  a = [[0,0]]
  for _ in range(n):
    x,y = map(int,input().split())
    a.append((x,y))
  d = [[0]*(k+1) for _ in range(n+1)]
  for i in range(1,n+1):
    for j in range(1,k+1):
      v = a[i][0]
      c = a[i][1]
      if v > j:
        d[i][j] = d[i-1][j]
      else:
        d[i][j] = max(d[i-1][j], d[i-1][j-v]+c)
  res = max([max(i) for i in d])
  print(f'#{t+1} {res}')