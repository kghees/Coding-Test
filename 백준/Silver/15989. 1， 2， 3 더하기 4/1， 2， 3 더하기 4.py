d = [1]*10001
for i in range(2, 10001):
  d[i] += d[i-2]
for i in range(3, 10001):
  d[i] += d[i-3]
for t in range(int(input())):
  n = int(input())
  print(d[n])