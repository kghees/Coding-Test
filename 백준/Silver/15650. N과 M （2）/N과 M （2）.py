def dfs(x,start):
  if x == m:
    print(*a)
    return
  for i in range(start, n+1):
    if not check[i]:
      check[i] = True
      a.append(i)
      dfs(x+1,i+1)
      check[i] = False
      a.pop()
n,m = map(int,input().split())
check = [False]*(n+1)
a = []
dfs(0,1)