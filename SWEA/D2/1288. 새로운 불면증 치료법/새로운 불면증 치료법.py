for t in range(int(input())):
  n = int(input())
  num = [0]*10
  a = 1
  while 0 in num:
    ans = str(n*a)
    for i in ans:
      num[int(i)] += 1
    a += 1
  print(f'#{t+1} {(a-1)*n}')