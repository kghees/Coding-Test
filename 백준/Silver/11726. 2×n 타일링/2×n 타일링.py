n = int(input())
d = [0]*(n+1)
if n <= 3:
  print(n)
else:
  d[1] = 1
  d[2] = 2
  for i in range(3, n+1):
      d[i] = d[i-1] + d[i-2]
  print(d[i] % 10007)