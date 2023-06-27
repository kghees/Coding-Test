while True:
  s = input()
  a = []
  if s == '.':
    break
  for i in s:
    if i == '(' or i == '[':
      a.append(i)
    elif i == ')':
      if len(a) != 0 and a[-1] == '(':
        a.pop()
      else:
        a.append(')')
        break
    elif i == ']':
      if len(a) != 0 and a[-1] == '[':
        a.pop()
      else:
        a.append(']')
        break
  if len(a) == 0:
    print('yes')
  else:
    print('no')