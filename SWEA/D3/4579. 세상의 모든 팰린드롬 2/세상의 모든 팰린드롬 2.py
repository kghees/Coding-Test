for t in range(int(input())):
  s = input()
  check = True
  if len(s) == 1:
    check = True
  else:
    for i in range(len(s)//2):
      if s[i] != s[-i-1]:
        if s[i] != '*' and s[-i-1] != '*':
          check = False
        break
  if check:
    print(f'#{t+1} Exist')
  else:
    print(f'#{t+1} Not exist')