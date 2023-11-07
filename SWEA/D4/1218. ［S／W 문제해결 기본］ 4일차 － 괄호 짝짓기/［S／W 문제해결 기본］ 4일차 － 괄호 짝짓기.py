for t in range(1,11):
  n = int(input())
  a = list(input())
  stack = []
  left = ['(','[','{','<']
  right = [')',']','}','>']
  for i in a:
    if i in left:
      stack.append(i)
    if i in right:
      if right.index(i) == left.index(stack[-1]):
        stack.pop()
      else:
        break
  if stack:
    print(f'#{t} 0')
  else:
    print(f'#{t} 1')