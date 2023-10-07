for t in range(int(input())):
  n,d = map(int,input().split())
  x = d*2 + 1
  result = n//x
  if n % x == 0:
    print(f'#{t+1} {result}')
  else:
    print(f'#{t+1} {result+1}')