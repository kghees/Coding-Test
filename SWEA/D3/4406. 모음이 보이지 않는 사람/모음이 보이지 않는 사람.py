for t in range(int(input())):
  s = list(input())
  x = ['a','e','i','o','u']
  ans = ''
  for i in range(len(s)):
    if s[i] in x:
      continue
    ans += s[i]
  print(f'#{t+1} {ans}')