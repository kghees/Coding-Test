for t in range(int(input())):
  s = input()
  a = 'abcdefghijklmnopqrstuvwxyz'
  cnt = 0
  for i in range(len(s)):
    if s[i] == a[i]:
      cnt += 1
    else:
      break
  print(f'#{t+1} {cnt}')