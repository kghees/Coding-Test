n = int(input())
a = list(map(int,input().split()))
d = [1]*n
for i in range(1, n):
  if a[i] >= a[i-1]:
    d[i] = d[i-1] + 1
d1 = [1]*n
for i in range(1, n):
  if a[i] <= a[i-1]:
    d1[i] = d1[i-1] + 1
print(max(max(d),max(d1)))