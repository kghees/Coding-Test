n = int(input())
a = list(map(int,input().split()))
d = [0]*n
for i in range(n):
  d[i] = a[i]
  if i == 0:
    continue
  if d[i] < d[i-1]+a[i]:
    d[i] = d[i-1]+a[i]
d1 = [0]*n
for i in range(n-1, -1, -1):
  d1[i] = a[i]
  if i == n-1:
    continue
  if d1[i] < d1[i+1]+a[i]:
    d1[i] = d1[i+1]+a[i]
ans = max(d)
for i in range(1, n-1):
  if ans < d[i-1] + d1[i+1]:
    ans = d[i-1] + d1[i+1]
print(ans)