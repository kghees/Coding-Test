for t in range(int(input())):
  n,a,b = map(int,input().split())
  m = -1
  for r in range(1, n+1):
    c = 1
    while r*c <= n:
      value = a*abs(r-c) + b*(n-r*c)
      if m == -1:
        m = value
      else:
        m = min(m,value)
      c += 1
  print(f'#{t+1} {m}')