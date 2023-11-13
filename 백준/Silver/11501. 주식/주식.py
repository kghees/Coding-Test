import sys
input = sys.stdin.readline
for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  a = a[::-1]
  x = 0
  res = 0
  for i in a:
    if x < i:
      x = i
    res += x - i
  if res > 0:
    print(res)
  else:
    print(0)