l = int(input())
for _ in range(l):
  left = []
  right = []
  s = input()
  for i in s:
    if i == '-':
      if left:
        left.pop()
    elif i == '<':
      if left:
        right.append(left.pop())
    elif i == '>':
      if right:
        left.append(right.pop())
    else:
      left.append(i)
  right.reverse()
  print(''.join(left+right))