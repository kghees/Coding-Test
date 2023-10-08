for t in range(int(input())):
  s = input()
  num = [0]*100
  for i in range(len(s)):
    num[i] = s.count(s[i])
  ans = []
  for i in range(len(s)):
    if num[i] % 2 != 0:
      if s[i] not in ans:
        ans.append(s[i])
  ans.sort()
  if ans:
    print(f'#{t+1}',end=' ')
    for i in ans:
      print(i,end='')
    print()
  else:
    print(f'#{t+1} Good')