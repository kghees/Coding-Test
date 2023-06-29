import sys
input = sys.stdin.readline
s = input().rstrip()
tag = False
result = ''
stack = []
for i in s:
  if i == ' ':
    for _ in range(len(stack)):
      result += stack.pop()
    result += i
  elif i == '<':
    tag = True
    for _ in range(len(stack)):
      result += stack.pop()
    result += i
  elif i == '>':
    tag = False
    result += i
  elif tag:
    result += i
  else:
    stack.append(i)

for _ in range(len(stack)):
  result += stack.pop()
print(result)