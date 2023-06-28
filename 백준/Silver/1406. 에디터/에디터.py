import sys
input = sys.stdin.readline
left = list(input().strip())
right = []
n = int(input())
for i in range(n):
  m = input().split()
  if m[0] == 'L' and left:
    right.append(left.pop())
  elif m[0] == 'D' and right:
    left.append(right.pop())
  elif m[0] == 'B' and left:
    left.pop()
  elif m[0] == 'P':
    left.append(m[1])
right.reverse()
print(''.join(left + right))