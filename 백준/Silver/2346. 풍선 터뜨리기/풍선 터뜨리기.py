import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
d = deque(enumerate(map(int, input().split())))
ans = []
while d:
  x,y = d.popleft()
  ans.append(x+1)
  if y > 0:
    d.rotate(-(y-1))
  elif y < 0:
    d.rotate(-y)
print(*ans)