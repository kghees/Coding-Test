from collections import defaultdict
for t in range(int(input())):
  n,m = map(int,input().split())
  a = defaultdict(list)
  for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
  result = 0
  for i in range(1, n+1):
    for j in range(i+1, n+1):
      for k in range(j+1, n+1):
        if i in a[j] and j in a[k] and k in a[i]:
          result += 1
  print(f'#{t+1} {result}')