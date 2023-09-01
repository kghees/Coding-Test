n = int(input())
a = list(map(int,input().split()))
d = [1]*n
for i in range(1, n):
  for j in range(i):
    if a[i] > a[j]:
      d[i] = max(d[i],d[j]+1)
d1 = [1]*n
a.reverse()
for i in range(1, n):
  for j in range(i):
    if a[i] > a[j]:
      d1[i] = max(d1[i], d1[j]+1)
d1.reverse()
d2 = [0]*n
for i in range(n):
  d2[i] = d[i] + d1[i]
print(max(d2)-1)