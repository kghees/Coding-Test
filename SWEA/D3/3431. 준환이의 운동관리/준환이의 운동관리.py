for t in range(int(input())):
  l,u,x = map(int,input().split())
  result = 0
  if l > x:
    result = l-x
  elif l <= x <= u:
    result = 0
  else:
    result = -1
  print(f'#{t+1} {result}')