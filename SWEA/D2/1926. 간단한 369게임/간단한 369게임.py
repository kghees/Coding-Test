n = int(input())
res = []
for i in range(1, n+1):
  x = str(i)
  a = x.count('3') + x.count('6') + x.count('9')
  if a == 0:
    res.append(i)
  else:
    res.append('-'*a)
print(*res)