n = int(input())
d = int(input())
a = []
for _ in range(n-1):
  a.append(int(input()))
a.sort(reverse=True)
cnt = 0
if n == 1:
  print(0)
else:
  while a[0] >= d:
    d += 1
    a[0] -= 1
    cnt += 1
    a.sort(reverse=True)
  print(cnt)