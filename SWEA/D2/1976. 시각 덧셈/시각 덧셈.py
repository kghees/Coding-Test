for t in range(int(input())):
  a, b, c, d = map(int,input().split())
  h = 0
  m = 0
  if a + c > 12:
    h = a + c
    h -= 12
  else:
    h = a + c
  if b + d > 60:
    h += 1
    m = b + d - 60
  else:
    m = b + d
  print(f'#{t+1} {h} {m}')