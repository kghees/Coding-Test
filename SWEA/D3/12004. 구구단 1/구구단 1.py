for t in range(int(input())):
  n = int(input())
  check = False
  for i in range(1, 10):
    for j in range(1, 10):
      if i*j == n:
        check = True
        break
  if check:
    print(f'#{t+1} Yes')
  else:
    print(f'#{t+1} No')