for t in range(1,11):
  n,num = input().split()
  stack = []
  for i in num:
    if not stack:
      stack.append(i)
    else:
      if stack[-1] == i:
        stack.pop()
      else:
        stack.append(i)
  print(f'#{t}',end=' ')
  for i in stack:
    print(i,end='')
  print()