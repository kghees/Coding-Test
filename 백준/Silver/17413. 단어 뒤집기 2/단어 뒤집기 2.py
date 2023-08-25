s = input()
stack = []
result = []
for i in range(len(s)):
  if s[i] == '>':
    stack.append('>')
    result.append(''.join(stack))
    stack = []
  elif s[i] == '<' and stack:
    stack.reverse()
    result.append(''.join(stack))
    stack = [s[i]]
  elif s[i] == ' ' and '<' not in stack:
    stack.reverse()
    result.append(''.join(stack))
    result.append(' ')
    stack = []
  else:
    stack.append(s[i])
if stack:
  stack.reverse()
  result.append(''.join(stack))
print(''.join(result))