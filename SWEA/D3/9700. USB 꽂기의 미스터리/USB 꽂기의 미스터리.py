for t in range(int(input())):
  p,q = map(float,input().split())
  x = (1-p)*(1-q)
  y = p*(1-q)*(1-q)
  if x < y:
    print(f'#{t+1} YES')
  else:
    print(f'#{t+1} NO')