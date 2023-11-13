n = int(input())
a = list(map(int,input().split()))
a.sort()
res = 0
for i in a:
  if n <= 1:
    break
  if i >= n-1:
    res += n-1
    break
  elif i == 1:
    n -= 2
    res += 1
  else:
    for j in range(i-1):
      n -= 1
      res += 1
    n -= 2
    res += 1
print(res)