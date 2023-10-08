for t in range(int(input())):
  s = list(input())
  result = [0]*len(s)
  for i in range(len(s)):
    result[i] = s.count(s[i])
  check = True
  for i in result:
    if i != 2:
      check = False
  if check:
    print(f'#{t+1} Yes')
  else:
    print(f'#{t+1} No')