for t in range(int(input())):
  a,b = map(int,input().split())
  res = (a//b)**2
  print(f'#{t+1} {res}')