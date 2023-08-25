n = int(input())
cnt = 0
for _ in range(n):
  s = input()
  stack = []
  for i in range(len(s)):
    if stack and s[i] == stack[-1]:
      stack.pop()
    else:
      stack.append(s[i])
  if len(stack) == 0:
    cnt += 1
print(cnt) 