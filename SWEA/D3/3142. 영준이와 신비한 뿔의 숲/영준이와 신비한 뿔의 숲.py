for t in range(int(input())):
  n,m = map(int,input().split())
  a,b = 0,0
  b = n-m
  a = m-b
  print(f'#{t+1} {a} {b}')