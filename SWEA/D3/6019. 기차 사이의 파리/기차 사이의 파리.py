for t in range(int(input())):
  d,a,b,f = map(int,input().split())
  x = d / (a+b)
  result = x*f
  print(f'#{t+1} {result:.10f}')