def dfs(x):
  global cnt
  if sum(ans) == k and len(ans) > 0:
    cnt += 1
  for i in range(x,n):
    ans.append(a[i])
    dfs(i+1)
    ans.pop()
for t in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  cnt = 0
  ans = []
  dfs(0)
  print(f'#{t+1} {cnt}')