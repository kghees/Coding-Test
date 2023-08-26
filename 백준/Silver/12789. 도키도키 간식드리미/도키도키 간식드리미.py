n = int(input())
s = list(map(int,input().split()))
stack = []
i = 1
while s:
  if s[0] == i:
    s.pop(0)
    i += 1
  else:
    stack.append(s.pop(0))
  while stack:
    if stack[-1] == i:
      stack.pop()
      i += 1
    else:
      break
if not stack:
  print('Nice')
else:
  print('Sad')