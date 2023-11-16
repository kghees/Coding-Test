for t in range(int(input())):
  n = int(input())
  num = [0]*10
  cnt = 1
  while True:
    if 0 not in num:
      break
    x = str(n*cnt)
    for i in x:
      num[int(i)] += 1
    cnt += 1
  print(f'#{t+1} {(cnt-1)*n}')