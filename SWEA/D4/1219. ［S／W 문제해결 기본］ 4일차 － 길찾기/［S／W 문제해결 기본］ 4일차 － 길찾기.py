def dfs(x):
  check[x] = 1
  for i in d[x]:
    if not check[i]:
      dfs(i)
  return
for _ in range(10):
  t,n = map(int,input().split())
  a = list(map(int,input().split()))
  d = [[] for _ in range(100)]
  for i in range(0,len(a),2):
    d[a[i]].append(a[i+1])
  check = [0]*100
  dfs(0)
  print(f'#{t} {check[99]}')