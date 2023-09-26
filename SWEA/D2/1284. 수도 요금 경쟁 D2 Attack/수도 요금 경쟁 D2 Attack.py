for t in range(int(input())):
  p,q,r,s,w = map(int,input().split())
  a = p * w
  if r > w:
    b = q
  else:
    b = q + (w-r)*s
  if a < b:
    print(f'#{t+1} {a}')
  else:
    print(f'#{t+1} {b}')