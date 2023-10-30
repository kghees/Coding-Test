for t in range(int(input())):
  d,l,n = map(int,input().split())
  res = 0
  for i in range(n):
    res += d*(1+i*(l*0.01))
  print(f'#{t+1} {int(res)}')