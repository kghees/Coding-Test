for t in range(int(input())):
  n,m,k = map(int,input().split())
  a = list(map(int,input().split()))
  a.sort()
  result = 'Possible'
  for i in range(n):
    cnt = (a[i] // m)*k - (i+1)
    if cnt < 0:
      result = 'Impossible'
      break
  print(f'#{t+1} {result}')