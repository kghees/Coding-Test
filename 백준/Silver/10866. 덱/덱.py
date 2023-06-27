#10866
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
d = deque()
for _ in range(n):
  s = input().split()
  if s[0] == 'push_front':
    d.appendleft(s[1])
  elif s[0] == 'push_back':
    d.append(s[1])
  elif s[0] == 'pop_front':
    if len(d) == 0:
      print(-1)
    else:
      print(d.popleft())
  elif s[0] == 'pop_back':
    if len(d) == 0:
      print(-1)
    else:
      print(d.pop())
  elif s[0] == 'size':
    print(len(d))
  elif s[0] == 'empty':
    if len(d) == 0:
      print(1)
    else:
      print(0)
  elif s[0] == 'front':
    if len(d) == 0:
      print(-1)
    else:
      print(d[0])
  elif s[0] == 'back':
    if len(d) == 0:
      print(-1)
    else:
      print(d[-1])