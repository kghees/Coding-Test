for t in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  res = []
  for i in range(1, n+1):
    if i not in a:
      res.append(i)
  res.sort()
  print(f'#{t+1}',*res)