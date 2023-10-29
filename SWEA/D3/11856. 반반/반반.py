for t in range(int(input())):
  s = input()
  res = [0]*4
  for i in range(4):
    res[i] = s.count(s[i])
  check = True
  for i in res:
    if i != 2:
      check = False
      break
  if check:
    print(f'#{t+1} Yes')
  else:
    print(f'#{t+1} No')