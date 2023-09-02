n = int(input())
a = list(map(int,input().split()))
d = [n+1]*n
d[0] = 0
for i in range(n):
  for j in range(1, a[i]+1):
    if i + j < n:
      d[i+j] = min(d[i]+1 ,d[i+j])
if d[n-1] == n+1:
  print(-1)
else:
  print(d[n-1])