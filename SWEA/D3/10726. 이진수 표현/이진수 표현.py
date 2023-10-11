for t in range(int(input())):
  n,m = map(int,input().split())
  x = (1<<n) - 1
  if (m&x) == x:
    print(f'#{t+1} ON')
  else:
    print(f'#{t+1} OFF')