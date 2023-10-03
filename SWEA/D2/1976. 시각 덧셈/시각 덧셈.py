for t in range(int(input())):
  a,b,c,d = map(int,input().split())
  h = a + c
  if h > 12:
    h -= 12
  m = b + d
  if m >= 60:
    h += 1
    m -= 60
  print(f'#{t+1} {h} {m}')