import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  s = input()
  stack = []
  for i in s:
    if i == ' ' or i == '\n':
      print(''.join(stack[::-1]),end='')
      stack.clear()
      print(i,end='')
    else:
      stack.append(i)