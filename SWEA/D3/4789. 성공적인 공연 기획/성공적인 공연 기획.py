for t in range(int(input())):
  a = input()
  cnt = int(a[0])
  res = 0
  x = 0
  for i in range(1,len(a)):
    if a[i] == 0:
      continue
    else:
      if i > cnt:
        res += i - cnt
        cnt = i + int(a[i])
      else:
        cnt += int(a[i])
  print(f'#{t+1} {res}')