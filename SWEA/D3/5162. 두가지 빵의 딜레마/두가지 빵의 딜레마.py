for t in range(int(input())):
  a,b,c = map(int,input().split())
  x = min(a,b)
  print(f'#{t+1} {c//x}')