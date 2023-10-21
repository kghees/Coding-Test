res = []
t = int(input())
for _ in range(t):
  n = int(input())
  while n > 9:
    n = sum(map(int,list(str(n))))
  res.append(n)
for k in range(t):
  print(f'#{k+1} {res[k]}')