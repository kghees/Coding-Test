for t in range(int(input())):
  n,m = map(int,input().split())
  a = [[] for _ in range(n+1)]
  for _ in range(m):
    x,y = map(int,input().split())
    a[x].append(y)
    a[y].append(x)
  cnt = 0
  for i in range(1,n+1):
    for j in range(i+1,n+1):
      for k in range(j+1,n+1):
        if i in a[j] and j in a[k] and k in a[i]:
          cnt += 1
  print(f'#{t+1} {cnt}')