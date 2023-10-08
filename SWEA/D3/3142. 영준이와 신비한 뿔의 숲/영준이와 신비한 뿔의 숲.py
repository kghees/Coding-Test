for t in range(int(input())):
  n,m = map(int,input().split())
  x = 2*m - n
  y = n - m
  print(f'#{t+1} {x} {y}')