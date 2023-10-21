for t in range(int(input())):
  a,b,c = map(int,input().split())
  x = 0
  if b-a == c-b:
    x = 0
  else:
    if b-a > c-b:
      x = ((b-a)-(c-b))/2
    else:
      x = ((c-b)-(b-a))/2
  print(f'#{t+1} {x:.1f}')