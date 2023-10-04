for t in range(int(input())):
  l,u,x = map(int,input().split())
  if l > x:
    print(f'#{t+1} {l-x}')
  elif l <= x <= u:
    print(f'#{t+1} {0}')
  else:
    print(f'#{t+1} {-1}')