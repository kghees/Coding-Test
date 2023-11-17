for t in range(10):
  n, m = input().split()
  stack = []
  for i in m:
    if not stack:
      stack.append(i)
    elif stack and stack[-1] == i:
      stack.pop()
    else:
      stack.append(i)
  print(f'#{t+1}',''.join(stack))