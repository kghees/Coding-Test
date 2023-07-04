n = int(input())
a = list(map(int,input().split()))
d = [0]*(n+1)
for i in range(n):
  d[i] = a[i]
for i in range(1, n):
  for j in range(i):
    if a[i] > a[j]:
      d[i] = max(d[i],d[j]+a[i])
print(max(d))