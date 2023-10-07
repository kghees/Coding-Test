for t in range(int(input())):
  p,q = input().split()
  p = float(p)
  q = float(q)
  a = (1-p)*(1-q)
  b = p*(1-q)*(1-q)
  if a < b:
    print(f'#{t+1} YES')
  else:
    print(f'#{t+1} NO')