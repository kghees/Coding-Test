for t in range(int(input())):
  n,m = map(int,input().split())
  a = [list(map(int,input().split())) for _ in range(n)]
  res = 0
  for i in range(n-m+1):
    for j in range(n-m+1):
      ans = 0
      for k in range(m):
        for l in range(m):
          ans += a[i+k][j+l]
      if res < ans:
        res = ans
  print(f'#{t+1} {res}')