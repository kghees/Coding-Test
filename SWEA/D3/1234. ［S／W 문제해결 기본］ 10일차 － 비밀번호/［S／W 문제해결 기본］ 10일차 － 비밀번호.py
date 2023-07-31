for t in range(1, 11):
  n, s = input().split()
  n = int(n)
  s = list(s)
  stack = []
  for i in s:
    if len(stack) == 0:
      stack.append(i)
    else:
      if stack[-1] == i:
        stack.pop()
      else:
        stack.append(i)
  print(f'#{t}',end=' ')
  for j in stack:
    print(j,end='')
  print()