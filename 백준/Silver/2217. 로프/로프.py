n = int(input())
a = []
for _ in range(n):
  m = int(input())
  a.append(m)
a.sort(reverse=True)
b = []
for i in range(n):
  sum = 0
  sum += a[i]*(i+1)
  b.append(sum)
print(max(b))