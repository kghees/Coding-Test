for t in range(int(input())):
  s = input()
  check = True
  if '?' not in s:
    if s == s[::-1]:
      print(f'#{t+1} Exist')
    else:
      print(f'#{t+1} Not exist')
  else:
    for i in range(len(s)//2):
      if s[i] == '?':
        continue
      elif s[i] == s[-i-1]:
        continue
      elif s[i] != s[-i-1]:
        if s[-i-1] == '?':
          continue
        else:
          check = False
          break
    if check:
      print(f'#{t+1} Exist')
    else:
      print(f'#{t+1} Not exist')