for t in range(int(input())):
  s = list(input())
  s.sort()
  stack = []
  for i in s:
    if stack and stack[-1] == i:
      stack.pop()
    else:
      stack.append(i)
  if stack:
    print(f'#{t+1} {"".join(stack)}')
  else:
    print(f'#{t+1} Good')