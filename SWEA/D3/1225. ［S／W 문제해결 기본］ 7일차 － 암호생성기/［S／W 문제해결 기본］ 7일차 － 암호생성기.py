for t in range(10):
  n = int(input())
  password = list(map(int,input().split()))
  i = 1
  while True:
    x = password.pop(0) - i
    if x > 0:
      password.append(x)
    else:
      password.append(0)
    if x <= 0:
      break
    i += 1
    if i > 5:
      i = 1
  print(f'#{t+1}',end=' ')
  print(*password)