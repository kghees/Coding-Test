for tc in range(int(input())):
  n, l = map(int,input().split())
  a = [[0,0]]
  for _ in range(n):
    t,k = map(int,input().split())
    a.append((t,k))
  d = [[0]*(l+1) for _ in range(n+1)]
  for i in range(1, n+1):
    for j in range(1,l+1):
      score = a[i][0]
      cal = a[i][1]
      if j < cal:
        d[i][j] = d[i-1][j]
      else:
        d[i][j] = max(d[i-1][j],d[i-1][j-cal]+score)
  result = max([max(i) for i in d])
  print(f'#{tc+1} {result}')