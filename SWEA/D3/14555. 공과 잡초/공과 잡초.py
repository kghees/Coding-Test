for t in range(int(input())):
  s = input()
  stack = []
  cnt = 0
  for i in range(len(s)):
    if s[i] == '(':
      stack.append('(')
    elif s[i] == '|':
      if stack and stack[-1] == '(':
        stack.pop()
        cnt += 1
      else:
        stack.append('|')
    elif s[i] == ')':
      if stack and stack[-1] == '|':
        stack.pop()
        cnt += 1
      elif stack and stack[-1] == '(':
        stack.pop()
        cnt += 1
  print(f'#{t+1} {cnt}')