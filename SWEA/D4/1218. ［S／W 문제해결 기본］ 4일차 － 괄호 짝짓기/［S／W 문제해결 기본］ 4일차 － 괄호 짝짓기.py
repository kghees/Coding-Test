for t in range(1,11):
  n = int(input())
  a = list(input())
  stack1 = []
  stack2 = []
  stack3 = []
  stack4 = []
  check = True
  for i in a:
    if i == '(':
      stack1.append('(')
    elif i == ')':
      if stack1 and stack1[-1] == '(':
        stack1.pop()
      else:
        check = False
        break
    elif i == '[':
      stack2.append('[')
    elif i == ']':
      if stack2 and stack2[-1] == '[':
        stack2.pop()
      else:
        check = False
        break
    elif i == '{':
      stack3.append('{')
    elif i == '}':
      if stack3 and stack3[-1] == '{':
        stack3.pop()
      else:
        check = False
        break
    elif i == '<':
      stack4.append('<')
    elif i == '>':
      if stack4 and stack4[-1] == '<':
        stack4.pop()
      else:
        check = False
        break
  if check and not stack1 and not stack2 and not stack3 and not stack4:
    print(f'#{t} 1')
  else:
    print(f'#{t} 0')