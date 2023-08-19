for t in range(10):
  n, password = input().split()
  n = int(n)
  password = list(password)
  stack = []
  for i in password:
    if len(stack) == 0:
      stack.append(i)
    else:
      if stack[-1] == i:
        stack.pop()
      else:
        stack.append(i)
  print(f'#{t+1}',end=' ')
  for i in stack:
    print(i,end='')
  print()