for t in range(int(input())):
  s = input()
  for i in range(1,10):
    if s[:i] == s[i:2*i]:
      print(f'#{t+1} {i}')
      break