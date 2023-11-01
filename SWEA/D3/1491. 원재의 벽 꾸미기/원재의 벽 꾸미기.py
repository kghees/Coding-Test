for t in range(int(input())):
  n,a,b = map(int,input().split())
  res = -1
  for r in range(1, n+1):
    c = 1
    while r*c<=n:
      x = a*abs(r-c) + b*(n-r*c)
      if res == -1:
        res = x
      else:
        res = min(x,res)
      c += 1
  print(f'#{t+1} {res}')