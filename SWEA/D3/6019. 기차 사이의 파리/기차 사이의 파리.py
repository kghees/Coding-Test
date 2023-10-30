for t in range(int(input())):
  d,a,b,f = map(int,input().split())
  res = (d/(a+b))*f
  print(f'#{t+1} {res:.10f}')