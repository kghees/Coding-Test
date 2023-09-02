n = int(input())
m = int(input())
a = [int(input()) for _ in range(m)]
d = [0]*(41)
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, 41):
  d[i] = d[i-1] + d[i-2]
result = 1
if m > 0:
  x = 0
  for i in range(m):
    result *= d[a[i]-1-x]
    x = a[i]
  result *= d[n-x]
else:
  result = d[n]
print(result)