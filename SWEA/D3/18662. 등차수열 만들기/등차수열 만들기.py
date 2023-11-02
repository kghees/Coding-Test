for t in range(int(input())):
  a,b,c = map(int,input().split())
  res = abs(b-(a+c)/2)
  print(f'#{t+1} {res:.1f}')