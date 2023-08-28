import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
  s = input().split()
  if s[0] == 'push':
    arr.append(s[1])
  elif s[0] == 'pop':
    if len(arr) == 0:
      print(-1)
    else:
      print(arr.pop())
  elif s[0] == 'size':
    print(len(arr))
  elif s[0] == 'empty':
    if len(arr) == 0:
      print(1)
    else:
      print(0)
  elif s[0] == 'top':
    if len(arr) == 0:
      print(-1)
    else:
      print(arr[-1])