for t in range(int(input())):
  n = int(input())
  a,b = 0, 0
  for i in range(1, 10):
    for j in range(1, 10):
      if i*j == n:
        a = i
        b = j
  if a != 0 and b != 0:
    print(f'#{t+1} Yes')
  else:
    print(f'#{t+1} No')