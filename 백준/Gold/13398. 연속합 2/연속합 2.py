import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
d = [0] * n
dr = [0] * n
for i in range(n):
  d[i] = a[i]
  dr[i] = a[i]
for i in range(n):
  if i == 0:
    continue
  d[i] = max(d[i-1] + a[i],a[i])

for i in range(n-1,-1,-1):
  if i == n-1:
    continue
  dr[i] = max(dr[i+1] + a[i], a[i])
ans = max(d)
for i in range(1, n-1):
  ans = max((d[i-1] + dr[i+1]),ans)
print(ans)