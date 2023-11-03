for t in range(int(input())):
  a,b = map(int,input().split())
  if a == b:
    print(f'#{t+1} {a}')
  else:
    print(f'#{t+1} 1')