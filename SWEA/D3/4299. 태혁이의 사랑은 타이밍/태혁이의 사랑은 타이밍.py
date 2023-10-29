for t in range(int(input())):
  d,h,m = map(int,input().split())
  res = 0
  if m - 11 < 0:
    h -= 1
    m += 60
  if h - 11 < 0:
    d -= 1
    h += 24
  if d - 11 < 0:
    res = -1
    print(f'#{t+1} {res}')
    break
  res += (d-11)*24*60 + (h-11)*60 + (m-11)
  print(f'#{t+1} {res}')