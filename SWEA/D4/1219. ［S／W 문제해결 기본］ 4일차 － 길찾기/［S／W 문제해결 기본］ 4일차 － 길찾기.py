def dfs(x):
  if x == 99:
    return True
  for i in d[x]:
     if not check[i]:
      check[i] = True
      if dfs(i):
        return True
for _ in range(1,11):
  t,n = map(int,input().split())
  a = list(map(int,input().split()))
  d = [[] for _ in range(100)]
  for i in range(0,len(a),2):
    d[a[i]].append(a[i+1])
  check = [False]*100
  check[0] = True
  if dfs(0):
    print(f'#{t} 1')
  else:
    print(f'#{t} 0')