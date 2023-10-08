for t in range(int(input())):
  s = input()
  stack = []
  cnt = 0 
  for i in s:
    if i == '(':
      stack.append('(')
    elif i == '|':
      if stack and stack[-1] == '(':
        cnt += 1
        stack.pop()
      else:
        stack.append('|')
    elif i == ')':
      if stack[-1] == '|':
        cnt += 1
        stack.pop()
      elif stack[-1] == '(':
        cnt += 1
        stack.pop()
    else:
      continue
  print(f'#{t+1} {cnt}')