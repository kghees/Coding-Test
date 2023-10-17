for t in range(int(input())):
  n,k = map(int,input().split())
  a = [[0,0]]
  d = [[0]*(k+1) for _ in range(n+1)]
  for _ in range(n):
    v,c = map(int,input().split())
    a.append((v,c))
  for i in range(1, n+1):
    for j in range(1, k+1):
      weight = a[i][0]
      value = a[i][1]
      if j < weight:
        d[i][j] = d[i-1][j]
      else:
        d[i][j] = max(d[i-1][j], d[i-1][j-weight] + value)
  result = max([max(i) for i in d])
  print(f'#{t+1} {result}')