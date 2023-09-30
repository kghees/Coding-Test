for t in range(int(input())):
  n = int(input())
  num = [0]*10
  cnt = 1
  while 0 in num:
    x = str(cnt * n)
    for i in x:
      num[int(i)] += 1
    cnt += 1
  print(f'#{t+1} {(cnt-1)*n}')