for t in range(int(input())):
  n,a,b = map(int,input().split())
  ma,mi = 0,0
  ma = min(a,b)
  if a + b >= n:
    mi = a + b - n
  else:
    mi = 0
  print(f'#{t+1} {ma} {mi}')