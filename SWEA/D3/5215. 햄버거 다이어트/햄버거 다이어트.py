for t in range(int(input())):
  n,l = map(int,input().split())
  a = [list(map(int,input().split())) for _ in range(n)]
  d = [[0]*l for _ in range(n)]
  for i in range(n):
    for j in range(l):
      score = a[i][0]
      cal = a[i][1]
      if j < cal:
        d[i][j] = d[i-1][j]
      else:
        d[i][j] = max(d[i-1][j], d[i-1][j-cal]+score)
  res = max([max(i) for i in d])
  print(f'#{t+1} {res}')