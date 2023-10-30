def alpha(x,ans):
  global cnt
  if x == n:
    res = set(ans)
    if len(res) == 26:
      cnt += 1
  else:
    alpha(x+1,ans+a[x])
    alpha(x+1,ans)
for t in range(int(input())):
  n = int(input())
  a = [input().rstrip() for _ in range(n)]
  cnt = 0
  alpha(0,'')
  print(f'#{t+1} {cnt}')