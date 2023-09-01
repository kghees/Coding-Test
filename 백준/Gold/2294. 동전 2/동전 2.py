n, k = map(int,input().split())
a = [int(input()) for _ in range(n)]
d = [10001]*(k+1)
d[0] = 0
for i in a:
  for j in range(i, k+1):
    if d[j] > 0:
      d[j] = min(d[j-i]+1, d[j])
if d[k] == 10001:
  print(-1)
else:
  print(d[k])