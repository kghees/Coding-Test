import sys
input = sys.stdin.readline
n, k = map(int,input().split())
a = [i for i in range(2, n+1)]
b = []
while len(a) > 0:
  x = a[0]
  c = []
  for i in range(len(a)):
    if a[i] % x == 0:
      b.append(a[i])
    else:
      c.append(a[i])
  a = c
print(b[k-1])