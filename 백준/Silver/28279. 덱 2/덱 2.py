import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
d = deque()
for i in range(n):
  a = list(map(int,input().split()))
  if a[0] == 1:
    d.appendleft(a[1])
  elif a[0] == 2:
    d.append(a[1])
  elif a[0] == 3:
    if d:
      print(d.popleft())
    else:
      print(-1)
  elif a[0] == 4:
    if d:
      print(d.pop())
    else:
      print(-1)
  elif a[0] == 5:
    print(len(d))
  elif a[0] == 6:
    if not d:
      print(1)
    else:
      print(0)
  elif a[0] == 7:
    if d:
      print(d[0])
    else:
      print(-1)
  elif a[0] == 8:
    if d:
      print(d[-1])
    else:
      print(-1)