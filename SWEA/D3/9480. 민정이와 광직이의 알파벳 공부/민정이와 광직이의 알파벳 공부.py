def dfs(x,ans):
  global cnt
  if x == n:
    k = set(ans)
    if len(k) == 26:
      cnt += 1
  else:
    dfs(x+1,ans+a[x])
    dfs(x+1,ans)
for t in range(int(input())):
  n = int(input())
  a = [input().rstrip() for _ in range(n)]
  cnt = 0
  dfs(0,'')
  print(f'#{t+1} {cnt}')