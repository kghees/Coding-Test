for t in range(int(input())):
  p,q,r,s,w = map(int,input().split())
  a = p * w
  if w > r:
    b = q + (w-r)*s
  else:
    b = q
  print(f'#{t+1} {min(a, b)}')