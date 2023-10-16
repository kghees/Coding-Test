for t in range(int(input())):
  n,m = map(int,input().split())
  a = [[] for _ in range(n+1)]
  for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
  cnt = 0
  for i in range(1, n+1):
    for j in a[i]:
      for k in a[j]:
        if k in a[i]:
          cnt += 1
  print(f'#{t+1} {cnt//6}')