s = list(input())
stack = []
res = 0
x = 1
for i in range(len(s)):
  if s[i] == '(':
    x *= 2
    stack.append(s[i])
  elif s[i] == '[':
    x *= 3
    stack.append(s[i])
  elif s[i] == ')':
    if not stack or stack[-1] != '(':
      res = 0
      break
    if s[i-1] == '(':
      res += x
    x //= 2
    stack.pop()
  elif s[i] == ']':
    if not stack or stack[-1] != '[':
      res = 0
      break
    if s[i-1] == '[':
      res += x
    x //= 3
    stack.pop()
if stack:
  print(0)
else:
  print(res)