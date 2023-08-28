left = list(input())
m = int(input())
right = []
for _ in range(m):
  s = list(input().split())
  if left and s[0] == 'L':
    right.append(left.pop())
  elif right and s[0] == 'D':
    left.append(right.pop())
  elif left and s[0] == 'B':
    left.pop()
  elif s[0] == 'P':
    left.append(s[1])
right.reverse()
print(''.join(left+right))