res = []
t = int(input())
for _ in range(t):
  n = input()
  while len(n) != 1:
    x = 0
    for i in range(len(n)):
      x += int(n[i])
    n = str(x)
  res.append(n)
for k in range(t):
  print(f'#{k+1} {res[k]}')