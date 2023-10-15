for t in range(int(input())):
  a = input()
  cnt = 0
  cnt += int(a[0])
  result = 0
  for i in range(1, len(a)):
    if a[i] == '0':
      continue
    else:
      if cnt >= i:
        cnt += int(a[i])
      else:
        result += i - cnt
        cnt = i + int(a[i])
  print(f'#{t+1} {result}')