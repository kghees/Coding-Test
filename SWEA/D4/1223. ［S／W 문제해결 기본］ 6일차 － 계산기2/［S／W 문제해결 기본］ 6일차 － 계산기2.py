for t in range(1,11):
  n = int(input())
  a = list(input())
  res = ''
  stack = []
  for i in a:
    if i == '+':
      while stack:
        res += stack.pop()
      stack.append(i)
    elif i == '*':
      while stack and stack[-1] == '*':
        res += stack.pop()
      stack.append(i)
    else:
      res += i
  while stack:
    res += stack.pop()
  stack = []
  for j in res:
    if j == '+':
      stack.append(stack.pop()+stack.pop())
    elif j == '*':
      stack.append(stack.pop()*stack.pop())
    else:
      stack.append(int(j))
  print(f'#{t} {stack[-1]}')