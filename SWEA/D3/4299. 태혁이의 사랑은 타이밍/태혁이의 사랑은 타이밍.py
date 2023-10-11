for t in range(int(input())):
  d,h,m = map(int,input().split())
  a,b,c = 11,11,11
  result = 0
  if m < c:
    h -= 1
    m += 60
  if h < b:
    d -= 1
    h += 24
  if d < a:
    print(f'#{t+1} -1')
    break
  x = d-a
  y = h-b
  z = m-c
  if x < 0:
    print(f'#{t+1} -1')
  else:
    result += (x*24*60) + (y*60) + z
    print(f'#{t+1} {result}')