br = list(input())
cnt = 0
stack = []
for i in range(len(br)):
  if br[i] == '(':
    stack.append('(')
  else:
    if br[i-1] == '(':
      stack.pop()
      cnt += len(stack)
    else:
      stack.pop()
      cnt += 1
print(cnt)  