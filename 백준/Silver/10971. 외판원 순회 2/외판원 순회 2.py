def dfs(start,next,ans,cnt):
  global res
  if cnt == n:
    if a[next][start]:
      ans += a[next][start]
      if res > ans:
        res = ans
    return
  if ans > res:
    return
  for i in range(n):
    if not check[i] and a[next][i]:
      check[i] = True
      dfs(start,i,ans+a[next][i],cnt+1)
      check[i] = False
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
res = 1e9
check = [False]*n
for i in range(n):
  check[i] = True
  dfs(i,i,0,1)
  check[i] = False
print(res)