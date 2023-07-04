n = int(input())
a = list(map(int,input().split()))
d = [1] * (n+1)
a.reverse()
for i in range(n):
  for j in range(i):
    if a[i] > a[j]:
      d[i] = max(d[i],d[j]+1)
d.reverse()
print(max(d))