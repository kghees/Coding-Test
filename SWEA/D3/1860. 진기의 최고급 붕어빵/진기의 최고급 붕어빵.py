for t in range(int(input())):
  n,m,k = map(int,input().split())
  a = list(map(int,input().split()))
  a.sort()
  result = True
  for i in range(n):
    x = (a[i]//m)*k - (i+1)
    if x < 0:
      result = False
      break
  if result:
    print(f'#{t+1} Possible')
  else:
    print(f'#{t+1} Impossible')