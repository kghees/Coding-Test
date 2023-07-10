import sys
input = sys.stdin.readline
t = int(input())
a = []
d = [0]*(t)
a = [int(input()) for _ in range(t)]
if len(a) <= 2:
  print(sum(a))
else:
  d[0] = a[0]
  d[1] = a[0]+a[1]
  d[2] = max(a[0]+a[2], a[1]+a[2])
  for i in range(3, t):
    d[i] = max(d[i-3]+a[i-1], d[i-2])+a[i]
  print(d[-1])