def every_sum(x):
  if sum(ans) >= b:
    res.append(sum(ans)-b)
  for i in range(x,n):
    ans.append(a[i])
    every_sum(i+1)
    ans.pop()
for t in range(int(input())):
  n,b = map(int,input().split())
  a = list(map(int,input().split()))
  ans = []
  res = []
  every_sum(0)
  print(f'#{t+1} {min(res)}')