n = int(input())
a = [0]*10001
for i in range(n):
  a[i] = int(input())
d = [0]*(10001)
d[0] = a[0]
d[1] = a[0] + a[1]
d[2] = max(a[1]+a[2], a[0]+a[2], d[1])
for i in range(3, n):
  d[i] = max(d[i-2]+a[i], d[i-3]+a[i-1]+a[i], d[i-1])
print(max(d))