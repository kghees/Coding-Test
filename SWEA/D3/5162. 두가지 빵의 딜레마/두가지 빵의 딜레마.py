for t in range(int(input())):
  a,b,c = map(int,input().split())
  x = min(a,b)
  res = c//x
  print(f'#{t+1} {res}')