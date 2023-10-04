for t in range(1,11):
  t = int(input())
  n,m = map(int,input().split())
  def dfs(n,cnt):
    if cnt == m:
      return n
    else:
      return n*dfs(n,cnt+1)
  result = dfs(n,1)
  print(f'#{t} {result}')