import sys
input = sys.stdin.readline
d = [0] * 1000001
d[1],d[2],d[3] = 1, 2, 4
for i in range(4, 1000001):
    d[i] = d[i-1]% 1000000009  + d[i-2]% 1000000009  + d[i-3]% 1000000009
for _ in range(int(input())):
  n = int(input())
  print(d[n] % 1000000009)