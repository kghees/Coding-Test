for t in range(int(input())):
  n,m = map(int,input().split())
  a = list(input().split())
  b = list(input().split())
  x = n + m
  c = a + b
  res = x - len(set(c))
  print(f'#{t+1} {res}')