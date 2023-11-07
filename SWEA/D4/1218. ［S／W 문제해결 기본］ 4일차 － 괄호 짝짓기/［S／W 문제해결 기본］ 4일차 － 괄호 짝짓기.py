for t in range(1,11):
  n = int(input())
  a = list(input())
  stack = []
  check = True
  for i in a:
    if i == '(':
      stack.append('(')
    elif i == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        check = False
        break
    elif i == '[':
      stack.append('[')
    elif i == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        check = False
        break
    elif i == '{':
      stack.append('{')
    elif i == '}':
      if stack and stack[-1] == '{':
        stack.pop()
      else:
        check = False
        break
    elif i == '<':
      stack.append('<')
    elif i == '>':
      if stack and stack[-1] == '<':
        stack.pop()
      else:
        check = False
        break
  if check and not stack:
    print(f'#{t} 1')
  else:
    print(f'#{t} 0')