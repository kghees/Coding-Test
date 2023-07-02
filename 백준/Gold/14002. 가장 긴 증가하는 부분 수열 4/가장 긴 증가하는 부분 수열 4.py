n = int(input())
a = list(map(int,input().split()))
d = [1] * (n)
for i in range(1,n):
  for j in range(i):
    if a[i] > a[j]:
      d[i] = max(d[i],d[j]+1)
print(max(d))
arr = []
m = max(d)
for i in range(n-1,-1,-1):
  if d[i] == m:
    arr.append(a[i])
    m -= 1
arr.reverse()
print(*arr)