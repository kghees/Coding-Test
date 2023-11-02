t = int(input())
res = []
for _ in range(t):
  n = input()
  x = n
  while len(x) > 1:
    k = 0
    for i in x:
      k += int(i)
    x = str(k)
  res.append(x)
for i in range(t):
  print(f'#{i+1} {res[i]}')