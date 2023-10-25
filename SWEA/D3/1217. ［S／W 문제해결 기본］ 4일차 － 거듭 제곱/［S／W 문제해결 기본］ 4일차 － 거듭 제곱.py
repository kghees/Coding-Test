def dfs(a,cnt):
  if cnt == b:
    return a
  else:
    return a*dfs(a,cnt+1)
for t in range(1, 11):
  n = int(input())
  a,b = map(int,input().split())
  print(f'#{t} {dfs(a,1)}')