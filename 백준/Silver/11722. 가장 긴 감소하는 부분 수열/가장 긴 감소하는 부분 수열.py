n = int(input())
a = list(map(int,input().split()))
d = [1]*n
for i in range(1, n):
  for j in range(i):
    if a[j] > a[i] and d[i] < d[j]+1:
      d[i] = d[j] + 1
print(max(d))