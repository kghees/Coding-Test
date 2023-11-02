for t in range(int(input())):
  n,m = map(int,input().split())
  a = list(input().split())
  b = list(input().split())
  x = n+m
  k = a+b
  res = x - len(set(k))
  print(f'#{t+1} {res}')