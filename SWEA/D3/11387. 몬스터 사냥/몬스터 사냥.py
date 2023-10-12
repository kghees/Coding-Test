for t in range(int(input())):
  d,l,n = map(int,input().split())
  result = 0
  x = l*0.01
  for i in range(n):
    result += d*(1+i*x)
  print(f'#{t+1} {int(result)}')