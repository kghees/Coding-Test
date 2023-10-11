for t in range(int(input())):
  s = input()
  a,b,c,d = 13,13,13,13
  check = True
  for i in range(len(s)):
    if s[i] == 'S':
      if s[i:i+3] in s[i+3:]:
        check = False
        break
      else:
        a -= 1
    elif s[i] == 'D':
      if s[i:i+3] in s[i+3:]:
        check = False
        break
      else:
        b -= 1
    elif s[i] == 'H':
      if s[i:i+3] in s[i+3:]:
        check = False
        break
      else:
        c -= 1
    elif s[i] == 'C':
      if s[i:i+3] in s[i+3:]:
        check = False
        break
      else:
        d -= 1
  if check:
    print(f'#{t+1} {a} {b} {c} {d}')
  else:
    print(f'#{t+1} ERROR')