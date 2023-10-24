for t in range(int(input())):
  s = list(input())
  res = []
  for i in range(len(s)):
    if s[i] not in 'aeiou':
      res.append(s[i])
  print(f'#{t+1}',''.join(res))